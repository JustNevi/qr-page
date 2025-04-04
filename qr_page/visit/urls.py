from django.urls import path
from . import views

urlpatterns = [
    path("<int:qr_id>", views.home, name="home")
]