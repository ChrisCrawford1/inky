from django.urls import path

from . import views

urlpatterns = [
    path("", views.view_pens, name="view_pens"),
    path("/create", views.create_pen, name="create_pen"),
    path("/<int:id>", views.show_pen, name="show_pen"),
    path("/update/<int:id>", views.update_pen, name="update_pen"),
]
