from django.urls import path

from . import views

app_name = "hotel"
urlpatterns = [
    path("", views.index, name="index"),
    path("hotel.html/", views.hotel, name="hotel"),
    path("hotel_search/", views.hotel_search, name="hotel_search"),
]