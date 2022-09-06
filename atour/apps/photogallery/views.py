from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from apps.photogallery.models import Album
from apps.photogallery.utils import DataMixin


class AlbumList(DataMixin, ListView):
    """Список альбомов"""
    model = Album
    template_name = 'photogallery/album_list.html'
    context_object_name = 'albums'   
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывода"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Фотогалерея')
        context.update(c_def)        
        return context


class AlbumDetail(DetailView):
    """Детальное формирование альбома"""
    model = Album
    template_name = 'photogallery/album_detail.html'
    slug_url_kwarg = 'album_slug'
    context_object_name = 'album'   
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывода"""
        context = super().get_context_data(**kwargs)
        return context
