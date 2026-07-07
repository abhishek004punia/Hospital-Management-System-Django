from django.urls import path
from . import views

urlpatterns = [
     path('add/', views.add_patient, name='add_patient'),

     path('list/', views.patient_list, name='patient_list'),

     path('view/<int:id>/', views.patient_detail, name='patient_detail'),

     path('edit/<int:id>/', views.edit_patient, name='edit_patient'),

     path('delete/<int:id>/', views.delete_patient, name='delete_patient'),
]