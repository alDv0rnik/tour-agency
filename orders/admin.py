from django.contrib import admin
from .models import Order, OrderInfo


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status')


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'shipping_address')