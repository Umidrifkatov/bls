
from django import template

register = template.Library()

@register.filter(name='replacer')
def replacer(value):
    return value.replace('\n', '<br />')