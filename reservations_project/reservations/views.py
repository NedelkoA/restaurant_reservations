from django.shortcuts import render, redirect
from .models import Reservation, Restaurant
from .forms import ReservationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from datetime import datetime


class RestaurantsView(ListView):
    model = Restaurant
    template_name = 'reservations/restaurants_list.html'


class ReservationsView(CreateView, DetailView):
    model = Restaurant
    form_class = ReservationForm
    template_name = 'reservations/reservation_seat.html'
    success_url = "/restaurants/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.filter(
            restaurant_id=self.kwargs['pk'], date=datetime.date(datetime.now()))
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)
        if form.is_valid():
            if Reservation.objects.filter(
                    date=form.cleaned_data['date'],
                    time=form.cleaned_data['time']).exists():
                return CreateView.get(self, request, *args, **kwargs)
        return CreateView.post(self, request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.restaurant = Restaurant.objects.filter(id=self.kwargs['pk'])[0]
        return super().form_valid(form)
