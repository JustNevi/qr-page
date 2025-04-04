from django.db import models

from dataclasses import dataclass
from typing import List

@dataclass
class RedirectButton:
    redirect_url: str
    text: str
    icon_url: str

@dataclass
class VisitPage:
    image_url: str
    title: str
    url_buttons: List[RedirectButton]

    def __post_init__(self):
        self.url_buttons = [RedirectButton(**url_button) for url_button in self.url_buttons]