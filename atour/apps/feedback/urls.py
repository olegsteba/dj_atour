from django.urls import path, re_path
from apps.feedback.views import FeedbackList


urlpatterns = [
    path('', FeedbackList.as_view(), name='feedback_list'),
    #path('add-feedback/', add_feedback, name='feedback_add'),
]
