from unicodedata import category
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from apps.service.models import Service, Category
from apps.service.utils import DataMixin


class ServiceList(DataMixin, ListView):
    """Весь список услуг"""
    model = Service
    template_name = 'service/service_list.html'
    context_object_name = 'services'
    allow_empty = False
    
    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывода"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Наши услуги')
        context.update(c_def)
        return context
    
    def get_queryset(self):
        """Выборка нужных данных"""
        #Опубликованные услуги
        return Service.objects.filter(is_published=True)
        

class ServiceCategory(DataMixin, ListView):
    """Весь список услуг определенной категории"""
    model = Service
    template_name = 'service/service_category.html'
    context_object_name = 'services'
    #allow_empty = False
    
    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывода"""
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(category), body=category.body)
        context.update(c_def)
        return context
    
    def get_queryset(self):
        """Выборка нужных данных"""
        #Опубликованные услуги определенной категории
        return Service.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)


class ServiceDetail(DataMixin, DetailView):
    """Детальный просмотр услуги"""
    model = Service
    template_name = 'service/service_detail.html'
    slug_url_kwarg = 'service_slug' 
    context_object_name = 'service'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывода"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context.update(c_def)
        return context
    