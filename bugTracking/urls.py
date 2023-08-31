from django.urls import path

from .views import bug

urlpatterns = [
    path('bugs', bug)
]
