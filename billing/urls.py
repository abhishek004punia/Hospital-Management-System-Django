from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_bill, name="add_bill"),
    path("list/", views.bill_list, name="bill_list"),
    path("view/<int:id>/", views.bill_detail, name="bill_detail"),
    path("edit/<int:id>/", views.edit_bill, name="edit_bill"),
]