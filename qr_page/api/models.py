from django.db import models

class RedirectButton(models.Model):
    redirect_url = models.CharField(max_length=200)
    text = models.CharField(max_length=15)
    icon_url = models.CharField(max_length=200)

class VisitPage(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    redirect_button = models.ForeignKey(RedirectButton, on_delete=models.CASCADE) 

