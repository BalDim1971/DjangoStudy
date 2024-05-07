from django.http import HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'women/index.html')


def about(request):
    return render(request, 'women/about.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
