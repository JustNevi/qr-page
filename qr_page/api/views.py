import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import VisitPage, RedirectButton

def home(request):
    return HttpResponse("Hello from API") 

# Checks is page exist, and if exists return page otherwise 404 page
def page_existence(func):
    def wrapper(request, qr_id, *args, **kwargs):
        if (VisitPage.objects.filter(id=qr_id).exists()):
            return func(request, qr_id, *args, **kwargs)
        else:
            return HttpResponse("404 No page")

    return wrapper

@page_existence
def get(request, qr_id):
    visit_page = VisitPage.objects.filter(id=qr_id)
    redirect_buttons = RedirectButton.objects.filter(visit_page__id=qr_id)

    json_visit_page = serializers.serialize("json", visit_page)
    json_redirect_buttons = serializers.serialize("json", redirect_buttons)
    json_visit_page = json.loads(json_visit_page)[0]["fields"]
    json_redirect_buttons = json.loads(json_redirect_buttons)
    buttons = []
    for button in json_redirect_buttons:
        fields = button["fields"]
        del fields["visit_page"] 
        buttons.append(fields)

    json_data = json_visit_page
    json_data["id"] = qr_id
    json_data["redirect_buttons"] = buttons 

    return JsonResponse(json_data) 
