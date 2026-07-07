from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.add_doctor, name='add_doctor'),
    path('list/', views.doctor_list, name='doctor_list'),
    path('view/<int:id>/', views.doctor_detail, name='doctor_detail'),

]