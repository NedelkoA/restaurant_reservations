from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'restaurants/$', views.RestaurantsView.as_view()),
    url(r'restaurants/add$', views.AddRestaurant.as_view(), name='add_restaurant'),
    url(r'restaurants/(?P<pk>[0-9])$', views.ReservationsView.as_view(), name='reservations'),
    url(r'restaurants/(?P<pk>[0-9])/create$', views.MakeReserve.as_view(), name='make_reservation'),
    url(r'restaurants/ratings$', views.RatingsRestaurants.as_view(), name='ratings_restaurants'),
]
