from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'page/404.html', status=404)


def main(request):
    context = {
        'tirle': 'Главная'
    }
    return render(request, 'page/main.html', context=context)

