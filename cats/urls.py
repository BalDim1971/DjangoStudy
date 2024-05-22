from django.urls import path, register_converter

from cats.views import categories, archive, show_category, show_tag_postlist
from cats.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', categories, name='cats'),  # http://127.0.0.1:8000/cats
    path('<slug:cat_slug>/', show_category, name='category'),
    path('archive/<year4:year>', archive, name='archive'),
    path('tag/<slug:tag_slug>/', show_tag_postlist, name='tag'),
]
