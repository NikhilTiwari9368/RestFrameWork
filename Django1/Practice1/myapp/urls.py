# myapp/urls.py
from django.urls import path
from .views import get_items

urlpatterns = [
    path('api/items/', get_items, name='get_items'),
]
