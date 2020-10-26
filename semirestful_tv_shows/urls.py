from django.urls import path, include
from shows import views

urlpatterns = [
    path("", views.root_redirect),
    path("shows/", include("shows.urls")),
]
