from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from datetime import datetime

from .models import User
from .models import Flights
from .forms import *

# Create your views here.
def index(request):
    user_list = User.objects.order_by("username")[:5]
    context = {
        "user_list": user_list,
    }
    return render(request, "flight/index.html", context)

def detail(request, username):
    user = get_object_or_404(User, pk=username)
    return render(request, "flight/detail.html", {"user": user})


def results(request, username):
    response = "You're looking at the name of username %s."
    return HttpResponse(response % username)


def vote(request, username):
    return HttpResponse("You're on username %s." % username)

def flight_search(request):
    if request.method == "POST":
        flight_to = request.POST.get("to")
        flight_from = request.POST.get("from")
        from_date = request.POST.get("date")
        db_date = datetime.strptime(from_date, '%Y-%m-%d')
        flight_airlines = request.POST.get("airlines")

        if not from_date and not flight_airlines and flight_to and flight_from:
            flight_list = Flights.objects.filter(departure_city=flight_from, arrival_city=flight_to)
        else:
            flight_list = Flights.objects.filter(departure_city=flight_from, arrival_city=flight_to, date=from_date, airlines=flight_airlines)

        context = {
            "flight_list": flight_list
        }
        return render(request, "flight/test.html", context)
    else:
        return HttpResponse('Invalid Request Method')
    
def login(request):
    return render(request, "flight/login.html")

def signup(request):
    return render(request, "flight/signup.html")

def flight(request):
    return render(request, "flight/flight.html")

def signup_user(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            newUser = form.save()
            newUser.save()
            return render(request, "flight/index.html")
        else:
            # Handle form validation errors
            # You can add error messages or other logic here
            # pass
            print(form.errors.as_text())
            return render(request, "flight/login.html")
    else:
        form = UserProfileForm()
        return render(request, "flight/test.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = get_object_or_404(User, pk=username)
        if password == user.password:
            return render(request, "flight/test.html")
    else:
        return render(request, "flight/login.html")
    
def makeComplaint(request):
    if request.method == "POST":
        form = NewComplaint(request.POST)
        if form.is_valid():
            newComplaint = form.save()
            return render(request, "flight/index.html")
        else:
            # Handle form validation errors
            # You can add error messages or other logic here
            # pass
            print(form.errors.as_text())
            return render(request, "flight/login.html")
    else:
        form = UserProfileForm()
        return render(request, "flight/test.html")
