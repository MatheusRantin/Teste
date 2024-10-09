from django.contrib import admin
from products import models
from . import models

# Register your models here.

@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'price',)
    search_fields = ('title',)
    list_filter = ('category', 'brand',)

admin.site.register(models.Product, ProductAdmin)
