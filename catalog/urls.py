from django.urls import path
from .views import *


app_name = 'catalog'

urlpatterns = [
    path("search/", get_tours, name="search_tour")
]


