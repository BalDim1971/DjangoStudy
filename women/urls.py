from django.urls import path, include

from women.views import index

urlpatterns = [
    path('', index),
]
