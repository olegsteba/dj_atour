from django.urls import path, re_path
from django.views.generic import TemplateView
from apps.page.views import main, PageDetail, PageCallback

urlpatterns = [
    path('', main, name='home'),
    path('search-tour/', TemplateView.as_view(template_name='page/search_tour.html')),
    path('callback/', PageCallback.as_view(), name='callback'),
    path('<slug:page_slug>/', PageDetail.as_view(), name='page'),
]
