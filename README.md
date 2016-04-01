# django-emojione
Wrapper for emojione emotion to use in django

```
pip install django-emojione
```


Settings:
```python
EMOJIPY_IMAGE_TYPE = 'png' # Or svg
EMOJIPY_IMAGE_PATH = 'path/to/emotion/graphics'
```

## Usage:
Simle usage
```python
from django_emojione import to_image
text = 'I want a luxury :hand_bag: \U1f602'
print to_image(text,  style="border:#F00 1px solid", css="a_css_class")
```

Use in template
```python
# In settings, add django_emojione
INSTALLED_APPS = (
    #...
    'django_emojione',
    #...
)

# In template file, register emojione
{% load emojione %}

{% to_image text  style="border:#F00 1px solid", css="a_css_class" %}
{% unicode_to_image text  style="border:#F00 1px solid", css="a_css_class" %}
```

For more information please check at http://emojione.com/
