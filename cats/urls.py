from django.urls import path, re_path, register_converter

from cats.views import categories, categories_get, categories_by_slug, archive
from cats.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', categories),
    path('<int:cat_id>/', categories_get),
    path('<slug:cat_slug>/', categories_by_slug),
    path('archive/<year4:year>', archive),
]
