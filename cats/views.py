from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse

from women.views import menu, data_db

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")


def categories_get(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категории</h1><p >id:{cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категории</h1><p >slug:"
                        f"{cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('sport',))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)
