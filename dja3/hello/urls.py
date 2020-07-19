from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("suru", views.suru, name="suru"),
    path("ninja", views.ninja, name="ninja"),
    path("<str:name>", views.greet, name="greet")
]