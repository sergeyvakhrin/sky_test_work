from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу индивидуальных предпринимателей """
    list_display = ['id', 'name', 'model_product', 'release_date']
