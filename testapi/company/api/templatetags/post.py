

from django import template

from ..models import Company

register = template.Library()

@register.simple_tag
def total_stu():
    return Company.objects.count()


# @register.inclusion_tag("tt.html")
# def show_latest(total=5):
#     last = Company.objects.order_by('-id')[:total]
#     return {'last' : last}



