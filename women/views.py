from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.template.defaultfilters import slugify

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Create your views here.
def index(request):
    data = {
        'title': 'главная страница',
        'main_title': 'main_title',
        'url': slugify("The Main Title 1"),
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'abc', True],
        'set': {1, 1, 2, 3, 2, 5},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20),
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
