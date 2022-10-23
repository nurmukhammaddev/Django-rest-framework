from django.urls import path, include
from .views import api_view

urlpatterns = [
    path('', api_view),
]
