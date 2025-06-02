from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:qr_id>", views.visit, name="visit")
]
