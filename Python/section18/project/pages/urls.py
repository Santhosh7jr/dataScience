from django.urls import path
from .views import home, display_lists

urlpatterns = [
    path("", display_lists)
]
