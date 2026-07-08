from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.add_appointment, name='add_appointment'),
    path('list/', views.appointment_list, name='appointment_list'),

]