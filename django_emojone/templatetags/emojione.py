__author__ = "phuong"
__date__ = "03 31 2016, 5:24 PM"

from django import template
from django.conf import settings

register = template.Library()

def to_image(val):
    return str(val) + '/parse emotion/'
    pass
