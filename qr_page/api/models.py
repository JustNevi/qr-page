from django.db import models

class VisitPage(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

class RedirectButton(models.Model):
    visit_page = models.ForeignKey(VisitPage, on_delete=models.CASCADE, related_name="redirect_buttons") 
    redirect_url = models.CharField(max_length=200)
    text = models.CharField(max_length=15)
    icon_url = models.CharField(max_length=200)


