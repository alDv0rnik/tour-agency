from django.urls import path
from .views import create_order


app_name = 'orders'

urlpatterns = [
    path("create_order/<slug:tour_slug>", create_order, name="create_order")
]