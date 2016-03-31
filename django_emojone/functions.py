__author__ = "phuong"
__date__ = "03 31 2016, 3:05 PM"

from django.conf import settings
from emojipy import Emoji

image_type = 'png'
if hasattr(settings, 'EMOJIPY_IMAGE_TYPE'):
    image_type = settings.EMOJIPY_IMAGE_TYPE

if hasattr(settings, 'EMOJIPY_SPRITES'):
    Emoji.sprites = settings.EMOJIPY_SPRITES

if hasattr(settings, 'EMOJIPY_SPRITES_PATH'):
    Emoji.image_path_svg_sprites = settings.EMOJIPY_SPRITES_PATH

Emoji.image_type = image_type
if hasattr(settings, 'EMOJIPY_IMAGE_PATH'):
    if image_type is 'png':
        Emoji.image_png_path = settings.EMOJIPY_IMAGE_PATH
    elif image_type is 'svg':
        Emoji.image_svg_path = settings.EMOJIPY_IMAGE_PATH


def to_image(text, **kwargs):
    """
    Parse short code and unicode code to emotion
    :param text:
    :param kwargs[css]: css class
    :param kwargs[style]: icon stylesheet
    :return: string
    """
    return Emoji.to_image(text, **kwargs)


def unicode_to_image(text, **kwargs):
    return Emoji.unicode_to_image(text, **kwargs)


def ascii_to_unicode(text, **kwargs):
    return Emoji.ascii_to_unicode(text, **kwargs)


def ascii_to_image(text, **kwargs):
    return Emoji.ascii_to_image(text, **kwargs)


def shortcode_to_image(text, **kwargs):
    return Emoji.shortcode_to_image(text, **kwargs)
