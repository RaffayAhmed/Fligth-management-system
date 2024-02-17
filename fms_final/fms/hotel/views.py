from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import Hotels

# Create your views here.
def index(request):
    return render(request, "flight/index.html")

def hotel(request):
    return render(request, "hotel/hotel.html")

def hotel_search(request):
    if request.method == "POST":
        city = request.POST.get("city")
        stars = request.POST.get("stars")
        room_type = request.POST.get("room-type")

        if not room_type and not stars and city:
            hotel_list = Hotels.objects.filter(city=city)
        else:
            if room_type == "single":
                hotel_list = Hotels.objects.filter(city=city, number_of_stars=stars, has_single_rooms=1)
            elif room_type == "double":
                hotel_list = Hotels.objects.filter(city=city, number_of_stars=stars, has_double_rooms=1)
            elif room_type == "deluxe":
                hotel_list = Hotels.objects.filter(city=city, number_of_stars=stars, has_deluxe_rooms=1)
            elif room_type == "suites":
                hotel_list = Hotels.objects.filter(city=city, number_of_stars=stars, has_suites=1)
            else:
                hotel_list = Hotels.objects.filter(city=city, number_of_stars=stars, has_presidential_suites=1)

        context = {
            "hotel_list": hotel_list
        }
        return render(request, "hotel/test.html", context)
    else:
        return HttpResponse('Invalid Request Method')