from django.db import models

from dataclasses import dataclass
from typing import List

@dataclass
class UrlButton:
    redirect_url: str
    text: str
    icon_url: str

@dataclass
class VisitPage:
    image_url: str
    title: str
    url_buttons: List[UrlButton]

    def __post_init__(self):
        self.url_buttons = [UrlButton(**url_button) for url_button in self.url_buttons]