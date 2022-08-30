from django.urls import path, re_path
from apps.page.views import main, page

urlpatterns = [
    path('', main, name='home'),
    path('<slug:page_slug>/', page, name="page"),
]
