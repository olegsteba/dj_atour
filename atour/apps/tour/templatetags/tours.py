from atexit import register
from django import template
from django.db.models import Count
from apps.tour.models import Tour


register = template.Library()

@register.inclusion_tag('tour/tour_last.html')
def last_tour(sort=None, count=3):
    if not sort:
        tours = Tour.objects[0:count]
    else:
        tours = Tour.objects.order_by(sort)[0:count]
    return {'tours': tours}


