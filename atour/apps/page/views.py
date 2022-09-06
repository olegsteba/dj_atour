#from msilib.schema import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from apps.page.models import Page


class PageDetail(DetailView):
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


def page_not_found(request, exception):
    return render(request, 'page/404.html', status=404)


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'page/main.html', context=context)    
