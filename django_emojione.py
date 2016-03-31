__author__ = "phuong"
__date__ = "03 31 2016, 3:05 PM"

from django.conf import settings
from emojipy import Emoji

image_type = 'png'
if settings.is_defined('EMOJIPY_IMAGE_TYPE'):
    image_type = settings.EMOJIPY_IMAGE_TYPE

if settings.is_defined('EMOJIPY_SPRITES'):
    Emoji.sprites = settings.EMOJIPY_SPRITES

if settings.is_defined('EMOJIPY_SPRITES_PATH'):
    Emoji.image_path_svg_sprites = settings.EMOJIPY_SPRITES_PATH

if settings.is_defined('EMOJIPY_IMAGE_TYPE'):
    Emoji.sprites = settings.EMOJIPY_SPRITES

Emoji.image_type = image_type
if settings.is_defined('EMOJIPY_IMAGE_PATH'):
    if image_type is 'png':
        Emoji.image_png_path = settings.EMOJIPY_IMAGE_PATH
    elif image_type is 'svg':
        Emoji.image_svg_path = settings.EMOJIPY_IMAGE_PATH


def to_image(text):
    return Emoji.to_image(text)


def unicode_to_image(text):
    return Emoji.unicode_to_image(text)


def ascii_to_unicode(text):
    return Emoji.ascii_to_unicode(text)


def ascii_to_image(text):
    return Emoji.ascii_to_image(text)
