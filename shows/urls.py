from django.urls import path
from . import views

urlpatterns = [
    path("new", views.add_new),
    path("create", views.create),
    path("<int:show_id>", views.this_show),
    path("<int:show_id>/edit", views.edit),
    path("<int:show_id>/update", views.update),
    path("<int:show_id>/destroy", views.destroy),
    path("", views.index),
]
