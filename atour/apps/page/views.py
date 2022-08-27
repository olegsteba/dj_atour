from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from apps.page.models import Page


def page_not_found(request, exception):
    return render(request, 'page/404.html', status=404)


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'page/main.html', context=context)


def page(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    
    context = {
        'page': page,
    }
    return render(request, 'page/page.html', context=context)
    
