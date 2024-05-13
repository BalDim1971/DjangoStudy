from django.urls import path, register_converter

from cats.views import categories, categories_by_slug, archive, show_category
from cats.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', categories, name='cats'),  # http://127.0.0.1:8000/cats
    # http://127.0.0.1:8000/cats/2
    path('<int:cat_id>/', show_category, name='category'),
    # http://127.0.0.1:8000/cats/fgfgd
    path('<slug:cat_slug>/', categories_by_slug, name='cats_slug'),
    # http://127.0.0.1:8000/cats/archive/2020
    path('archive/<year4:year>', archive, name='archive'),
]
