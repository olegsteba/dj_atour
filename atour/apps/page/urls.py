from django.urls import path
from apps.page.views import main

urlpatterns = [
    path('', main, name='home'),
]