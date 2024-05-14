from django.urls import path, register_converter

from cats.views import categories, categories_by_slug, archive, show_category
from cats.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', categories, name='cats'),  # http://127.0.0.1:8000/cats
    path('<slug:cat_slug>/', show_category, name='category'),
    path('archive/<year4:year>', archive, name='archive'),
]
