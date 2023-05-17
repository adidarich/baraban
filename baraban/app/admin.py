from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_category', 'is_published')
    list_filter = ('product_category', 'is_published')
    search_fields = ('name', 'id')
    search_help_text = 'Введите название товара или id товара'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'storage_device_and_ram', 'price', 'category')
    list_filter = ('status', 'category')
    search_fields = ('title', 'id', 'price')
    search_help_text = 'заголовок/id/цена'