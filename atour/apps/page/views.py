#from msilib.schema import ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from apps.page.forms import CallbackForm
from apps.page.models import Page
from apps.page.utils import DataMixin


class PageDetail(DataMixin, DetailView):
    """Формирование страницы для показа"""
    model = Page
    template_name = 'page/page.html'
    slug_url_kwarg = 'page_slug'
    context_object_name = 'page'   
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывода"""
        context = super().get_context_data(**kwargs)
        return context


class PageCallback(DataMixin, SuccessMessageMixin, CreateView):
    """Формирует форму добавления книги"""
    form_class = CallbackForm
    template_name = 'page/callback.html'
    success_url = reverse_lazy('callback')
    success_message = 'Спасибо за Ваше обращение. Наши специалисты свяжутся с Вами в ближайшее время.'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывода"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заказать обратный звонок')
        context.update(c_def)
        return context


def page_not_found(request, exception):
    return render(request, 'page/404.html', status=404)


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'page/main.html', context=context)    
