import json
from django.conf import settings

def get_visit_pages():
    json_path = str(settings.BASE_DIR) + "/visit_pages.json"
    with open(json_path, "r") as f:
        visit_pages = json.loads(f.read())

    return visit_pages