from django.contrib import admin

from products.models import Product, Warehouse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу индивидуальных предпринимателей """
    list_display = ['id', 'name', 'model_product', 'description', 'is_published', 'release_date']


@admin.register(Warehouse)
class ProductAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу индивидуальных предпринимателей """
    list_display = ['id', 'user', 'product', 'quantity', 'price']
