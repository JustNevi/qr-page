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
    redirect_buttons: List[RedirectButton]

    def __post_init__(self):
        self.redirect_buttons = [RedirectButton(**redirect_button) for redirect_button in self.redirect_buttons]