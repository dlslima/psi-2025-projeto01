from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("atores/", views.atores, name="atores"),
    path("sobre/", views.sobre, name="sobre"),
]