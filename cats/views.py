from django.http import HttpResponse

# Create your views here.

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")


def categories_get(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категории</h1><p >id:{cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категории</h1><p >slug:"
                        f"{ cat_slug }</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")
