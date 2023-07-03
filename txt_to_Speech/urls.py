from django.urls import path
from .views import prompt,audio

urlpatterns = [
    path('',prompt,name="query"),
    path('audio/',prompt,name="query")
]