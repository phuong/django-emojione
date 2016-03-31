# django-emojione
Wrapper for emojione to use in django

```
pip install django-emojione
```


Settings:
```
EMOJIPY_IMAGE_TYPE = 'png' # Or svg
EMOJIPY_IMAGE_PATH = 'path/to/emotion/graphics'
```

Usage:
```
from django_emojione import to_image
text = 'I want a luxury :hand_bag: '
print to_image(text,  style="border:#F00 1px solid", css="a_css_class")
```

For more information please check at http://emojione.com/