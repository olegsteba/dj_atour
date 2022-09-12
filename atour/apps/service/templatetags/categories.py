from django import template
from django.db.models import Count
from apps.service.models import Service, Category


register = template.Library()

@register.inclusion_tag('service/categories_grid.html')
def show_categories_grid():
    categories = Category.objects.annotate(Count('category_services')).filter(is_published=True).order_by('position')
    return {
        'categories': categories
    }
