from django.urls import path, re_path
from apps.page.views import main, PageDetail

urlpatterns = [
    path('', main, name='home'),
    path('<slug:page_slug>/', PageDetail.as_view(), name="page"),
]
