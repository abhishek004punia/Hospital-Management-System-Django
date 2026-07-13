from django.urls import path

from . import views


urlpatterns = [

    path(
        "add/",
        views.add_medicine,
        name="add_medicine"
    ),

    path(
        "list/",
        views.medicine_list,
        name="medicine_list"
    ),

    path(
        "detail/<int:id>/",
        views.medicine_detail,
        name="medicine_detail"
    ),

    path(
        "edit/<int:id>/",
        views.edit_medicine,
        name="edit_medicine"
    ),

    path(
        "delete/<int:id>/",
        views.delete_medicine,
        name="delete_medicine"
    ),

]
