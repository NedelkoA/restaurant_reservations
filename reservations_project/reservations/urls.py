from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^restaurants/$', views.RestaurantsView.as_view()),
    url(r'^restaurants/(?P<pk>[0-9])$', views.ReservationsView.as_view()),
]
