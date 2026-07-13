from django.urls import path

from . import views


urlpatterns = [

    path(
        "add/",
        views.add_lab_test,
        name="add_lab_test"
    ),

    path(
        "list/",
        views.lab_test_list,
        name="lab_test_list"
    ),

    path(
        "detail/<int:id>/",
        views.lab_test_detail,
        name="lab_test_detail"
    ),

    path(
        "edit/<int:id>/",
        views.edit_lab_test,
        name="edit_lab_test"
    ),

    path(
        "delete/<int:id>/",
        views.delete_lab_test,
        name="delete_lab_test"
    ),

]