from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.add_appointment, name='add_appointment'),
    path('list/', views.appointment_list, name='appointment_list'),
    path('view/<int:id>/', views.appointment_detail, name='appointment_detail'),
    path('edit/<int:id>/', views.edit_appointment, name='edit_appointment'),
    path('delete/<int:id>/', views.delete_appointment, name="delete_appointment"),

]