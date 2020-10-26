from django.urls import path
from . import views

urlpatterns = [
    path("new", views.add_new),
    path("create", views.create),
    path("<int:show_id>", views.this_show),
    # path(
    #     "",
    # ),
    # path(
    #     "<>/edit",
    # ),
    # path(
    #     "<>/update",
    # ),
    # path(
    #     "<>/destroy",
    # ),
    path("", views.index),
]
