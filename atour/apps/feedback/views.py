from urllib import request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from apps.feedback.models import Feedback
from apps.feedback.forms import FeedbackForm
from apps.feedback.utils import DataMixin


class FeedbackList(DataMixin, SuccessMessageMixin, FormMixin, ListView):
    """Все отзывы"""
    model = Feedback
    template_name = 'feedback/feedback_list.html'
    context_object_name = 'feedbacks'
    allow_empty = False
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback_list')
    success_message = 'Благодорим Вас за оставленный отзыв о нашем агенстве.'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
               
    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывод"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Отзывы')
        context.update(c_def)
        return context
    
    def get_queryset(self):
        """Вывод нужных данных"""
        return Feedback.objects.filter(is_published=True)



