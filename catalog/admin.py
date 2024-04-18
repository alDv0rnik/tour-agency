from django.contrib import admin
from .models import Category, Tour
from django.utils.safestring import mark_safe


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "destination", "price")
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields =[
        "created_at",
        "get_image"
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="110" height="110" />')


    get_image.short_description = "Image"

