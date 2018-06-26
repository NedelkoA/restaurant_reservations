from django.shortcuts import redirect, render
from .models import Reservation, Restaurant
from .forms import ReservationForm, RestaurantForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from datetime import datetime, timedelta
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import models
from .tasks import send_notification_email
from .utils.date_conversion import DateConversion


class RestaurantsView(ListView):
    model = Restaurant
    template_name = 'reservations/restaurants_list.html'


class AddRestaurant(CreateView):
    form_class = RestaurantForm
    template_name = 'reservations/add_restaurant.html'
    success_url = '/restaurants/'

    def form_valid(self, form):
        if Restaurant.objects.filter(title=form.cleaned_data['title']):
            messages.add_message(self.request, messages.INFO,
                                 'This restaurant already is create.')
            return redirect('add_restaurant')
        return super().form_valid(form)


class ReservationsView(DetailView):
    model = Restaurant
    template_name = 'reservations/reservation_table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.filter(
            restaurant=self.get_object(),
            date=datetime.date(datetime.now()))
        context['form'] = ReservationForm(
            instance=Restaurant.objects.get(id=self.kwargs['pk']))
        return context


class MakeReserve(CreateView):
    form_class = ReservationForm
    template_name = 'reservations/reservation_table.html'

    def form_valid(self, form):
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        date_conv = DateConversion(
            form.cleaned_data['date'],
            form.cleaned_data['time']
        )
        if Reservation.objects.filter(
                restaurant_id=self.kwargs['pk'],
                date=form.cleaned_data['date'],
                time__gt=date_conv.hour_before_reserve,
                time__lt=date_conv.hour_after_reserve,
                table=form.cleaned_data['table']).exists():
            messages.add_message(self.request, messages.INFO,
                                 'This time or table is reserved. '
                                 'Choose other time, date or table.')
            return redirect('reservations', pk=self.kwargs['pk'])
        elif datetime.now() > date_conv.reserve_time:
            messages.add_message(self.request, messages.INFO,
                                 'This time is past. ')
            return redirect('reservations', pk=self.kwargs['pk'])
        send_notification_email.apply_async([
            form.cleaned_data['contact_email'],
            Restaurant.objects.get(id=self.kwargs['pk']).title],
            eta=date_conv.reserve_time - timedelta(hours=1)
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(
            self.request,
            'reservations/date_input_error.html',
            {'pk': self.kwargs['pk']}
        )

    def get_success_url(self, **kwargs):
        return reverse_lazy('reservations', kwargs={'pk': self.kwargs['pk']})


class RatingsRestaurants(ListView):
    template_name = 'reservations/ratings.html'
    model = Restaurant

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all().annotate(
            rating=models.Count('reservations')).order_by('-rating')
