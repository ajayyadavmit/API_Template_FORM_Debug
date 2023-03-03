from django import template
from ..models import FlowerDB

register = template.Library()

@register.simple_tag
def total_flower():
    return FlowerDB.objects.count()


