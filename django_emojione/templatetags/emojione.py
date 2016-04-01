__author__ = "phuong"
__date__ = "03 31 2016, 5:24 PM"

from django import template
from emojipy import Emoji

register = template.Library()


@register.simple_tag
def to_image(value, *args, **kwargs):
    return Emoji.to_image(value, **kwargs)


@register.simple_tag
def unicode_to_image(value, *args, **kwargs):
    return Emoji.unicode_to_image(value, **kwargs)


@register.simple_tag
def shortcode_to_image(value, *args, **kwargs):
    return Emoji.shortcode_to_image(value, **kwargs)


@register.simple_tag
def ascii_to_image(value, *args, **kwargs):
    return Emoji.ascii_to_image(value, **kwargs)


@register.simple_tag
def shortcode_to_unicode(value, *args, **kwargs):
    return Emoji.ascii_to_image(value, **kwargs)
