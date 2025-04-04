from django.shortcuts import render, HttpResponse

from .models import VisitPage

from .componets.json_db import get_visit_pages

# Checks is page exist, and if exists return page otherwise 404 page
def page_existence(func):
    def wrapper(request, qr_id, *args, **kwargs):
        pages = get_visit_pages()
        print(qr_id)
        if (str(qr_id) in pages):
            return func(request, qr_id, *args, **kwargs)
        else:
            return HttpResponse("404 No page")

    return wrapper

@page_existence
def home(request, qr_id):
    pages = get_visit_pages()
    # Get requested page from json and convert to dataclass
    page = VisitPage(**pages[str(qr_id)])

    return HttpResponse(str(page))
