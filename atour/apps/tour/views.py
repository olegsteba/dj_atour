from django.views.generic import ListView, DetailView
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
        

class TourDetail(DataMixin, DetailView):
    """Детальный просмотр тура"""
    model = Tour
    template_name = 'tour/tour_detail.html'
    slug_url_kwarg = 'tour_slug' 
    context_object_name = 'tour'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        """Формируем контекст для вывода"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context.update(c_def)
        return context