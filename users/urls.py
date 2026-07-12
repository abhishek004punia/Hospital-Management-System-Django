from django.urls import path
from . import views

urlpatterns = [

    path("login/", views.login_view, name="login"),

    path("logout/", views.logout_view, name="logout"),
    path("doctor-dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
    path("reception-dashboard/", views.reception_dashboard, name="reception_dashboard"),
    path('profile/',views.profile, name="profile"),
    path(
    "change-password/",
    views.change_password,
    name="change_password"),

]