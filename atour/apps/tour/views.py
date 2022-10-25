from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from apps.tour.forms import OrderForm
from apps.tour.models import Tour
from apps.tour.utils import DataMixin


class TourList(DataMixin, ListView):
    """Все туры"""
    model = Tour
    template_name = 'tour/tour_list.html'
    context_object_name = 'tours'
    allow_empty = False
    
    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывода"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Горящие туры')
        context.update(c_def)
        return context
    
    def get_queryset(self):
        """Выборка нужных данных"""
        #Опубликованные туты
        return Tour.objects.filter(is_published=True)
        

class TourDetail(DataMixin, SuccessMessageMixin, FormMixin, DetailView):
    """Детальный просмотр тура"""
    model = Tour
    template_name = 'tour/tour_detail.html'
    slug_url_kwarg = 'tour_slug' 
    context_object_name = 'tour'
    allow_empty = False
    form_class = OrderForm
    success_message = 'Благодорим Вас за заказ. Специалисты свяжутся с Вами в ближайшее время.'    
    
    def get_success_url(self):
        return reverse_lazy('tour_detail', kwargs={'tour_slug':self.get_object().slug})
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.tour = self.get_object()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывода"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context.update(c_def)
        return context