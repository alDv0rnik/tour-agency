from django.urls import path
from .views import *


app_name = 'catalog'

urlpatterns = [
    path("search/", get_tours, name="search_tour"),
    path("tours/", TourListView.as_view(), name="tour_list"),
    path("tour/<slug:tour_slug>", TourDetailView.as_view(), name="tour_detail")
]


