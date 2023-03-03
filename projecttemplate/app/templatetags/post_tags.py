from django import template

from ..models import Student

register = template.Library()

@register.simple_tag
def total_stu():
    return Student.objects.count()


@register.inclusion_tag("latest.html")
def show_latest(total=5):
    last = Student.objects.order_by('-id')[:total]
    return {'last' : last}

