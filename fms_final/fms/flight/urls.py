from django.urls import path

from . import views

app_name = "flight"
urlpatterns = [
    path("", views.index, name="index"),
    path("specifics/<str:username>/", views.detail, name="detail"),
    path("<str:username>/results/", views.results, name="results"),
    path("<str:username>/vote/", views.vote, name="vote"),

    path("search-flights/", views.flight_search, name="flight_search"),
    path("login.html/", views.login, name="login"),
    path("signup.html/", views.signup, name="signup"),
    path("flight.html/", views.flight, name="flight"),
    path("user_login/", views.login_user, name="login_user"),
    path("user_signup/", views.signup_user, name="signup_user"),
    path("complaint/", views.makeComplaint, name="makeComplaint"),
]