from django.urls import path, re_path
from apps.page.views import main, page

urlpatterns = [
    re_path(r'^(?P<page_slug>[-_\w\d]+)', page, name='page'),
    path('', main, name='home'),
]