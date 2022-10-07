from atexit import register
from django import template
from django.db.models import Count
from apps.feedback.models import Feedback


register = template.Library()

@register.inclusion_tag('feedback/feedback_last.html')
def last_feedback(sort=None, count=3):
    if not sort:
        feedbacks = Feedback.objects.filter(is_published=True)[0:count]
    else:
        feedbacks = Feedback.objects.filter(is_published=True).order_by(sort)[0:count]
    return {'feedbacks': feedbacks}


