from django.contrib import admin
from .models import Category, Product, Order


class ProductTabularInline(admin.TabularInline):
    model = Product


class AppAdminSite(admin.AdminSite):
    site_header = 'SITE HEADER'
    site_title = 'SITE TITLE'
    index_title = 'INDEX TITLE'


appadmin = AppAdminSite(name='appadmin')


@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации ')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    list_display = ('name', 'product_category', 'is_published')
    list_filter = ('product_category', 'is_published')
    search_fields = ('name', 'id')
    search_help_text = 'Введите название товара или id товара'
    inlines = (ProductTabularInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    list_display = ('title', 'storage_device_and_ram', 'price', 'category', 'is_published')
    list_filter = ('status', 'category', 'is_published')
    search_fields = ('title', 'id', 'price')
    search_help_text = 'заголовок/id/цена'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'is_paid', 'date_created')
    list_filter = ('is_paid',)
    date_hierarchy = 'date_created'
    readonly_fields = ('date_created',)


appadmin.register(Category, CategoryAdmin)
appadmin.register(Product, ProductAdmin)
appadmin.register(Order, OrderAdmin)
