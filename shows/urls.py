from django.urls import path
from . import views

urlpatterns = [
    path("new", views.add_new),
    # path(
    #     "create",
    # ),
    # path(
    #     "<>",
    # ),
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
