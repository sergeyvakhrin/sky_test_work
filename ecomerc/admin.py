from django.contrib import admin

from ecomerc.models import Factory, Retail, Individual
from products.models import Product, Warehouse


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу Заводов """
    list_display = ['id', 'user_name', 'user_email', 'product_list', 'created_at']
    list_display_links = ['id', 'user_name', 'user_email', 'product_list', 'created_at']

    # TODO: При создании записи таблицы сделать выборку user клиентов только Завод

    def get_readonly_fields(self, request, obj=None):
        """ Делаем поля только для чтения, если просмотр """
        if obj:
            return self.readonly_fields + ('user',)
        return self.readonly_fields

    @admin.display(description='Название завода')
    def user_name(self, warehouse: Warehouse):
        """ Выводим наименование Завода """
        return warehouse.user.name

    @admin.display(description='Электронная почта')
    def user_email(self, warehouse: Warehouse):
        """ Выводим почту Завода """
        return warehouse.user.email

    @admin.display(description='Список товаров')
    def product_list(self, warehouse: Warehouse):
        """ Выводим список продуктов конкретного завода """
        if warehouse:
            warehouses = Warehouse.objects.filter(user=warehouse.user)
            products_name = []
            for warehous in warehouses:
                products_name.append(warehous.product.name)
            if len(products_name) > 0:
                return products_name
        return 'Нет продуктов'


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу Розничных сетей """
    list_display = ['id', 'user_name', 'user_email', 'product_list', 'created_at', 'supplier', 'debt']
    list_display_links = ['id', 'user_name', 'user_email', 'product_list', 'created_at', 'supplier', 'debt']
    exclude = ['product']
    readonly_fields = ['debt']

    def get_readonly_fields(self, request, obj=None):
        """ Делаем поля только для чтения, если просмотр """
        if obj:
            return self.readonly_fields + ['user', 'supplier']
        return self.readonly_fields

    # TODO: При создании записи таблицы сделать выборку user клиентов только Розничная сеть

    @admin.display(description='Название Сети')
    def user_name(self, warehouse: Warehouse):
        """ Выводим наименование Розничной сети """
        return warehouse.user.name

    @admin.display(description='Электронная почта')
    def user_email(self, warehouse: Warehouse):
        """ Выводим почту Розничной сети """
        return warehouse.user.email

    @admin.display(description='Список товаров')
    def product_list(self, warehouse: Warehouse):
        """ Выводим список продуктов конкретной Розничной сети """
        if warehouse:
            warehouses = Warehouse.objects.filter(user=warehouse.user)
            products_name = []
            for warehous in warehouses:
                products_name.append(warehous.product.name)
            if len(products_name) > 0:
                return products_name
        return 'Нет продуктов'


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу Индивидуальных Предпринимателей """
    list_display = ['id', 'user_name', 'user_email', 'product_list', 'created_at', 'supplier', 'debt']
    list_display_links = ['id', 'user_name', 'user_email', 'product_list', 'created_at', 'supplier', 'debt']
    exclude = ['product']
    readonly_fields = ['debt']

    def get_readonly_fields(self, request, obj=None):
        """ Делаем поля только для чтения, если просмотр """
        if obj:
            return self.readonly_fields + ['user', 'supplier']
        return self.readonly_fields

    # TODO: При создании записи таблицы сделать выборку user клиентов только Индивидуальный предприниматель

    @admin.display(description='Название ИП')
    def user_name(self, product: Product):
        """ Выводим наименование ИП """
        return product.user.name

    @admin.display(description='Электронная почта')
    def user_email(self, product: Product):
        """ Выводим почту ИП """
        return product.user.email

    @admin.display(description='Список товаров')
    def product_list(self, warehouse: Warehouse):
        """ Выводим список продуктов конкретного ИП """
        if warehouse:
            warehouses = Warehouse.objects.filter(user=warehouse.user)
            products_name = []
            for warehous in warehouses:
                products_name.append(warehous.product.name)
            if len(products_name) > 0:
                return products_name
        return 'Нет продуктов'
