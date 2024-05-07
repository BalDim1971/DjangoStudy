from django.urls import path

from women.views import index, about

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('about/', about, name='about'),  # http://127.0.0.1:8000/about
]
