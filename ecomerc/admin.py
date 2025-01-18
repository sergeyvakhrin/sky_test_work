from django.contrib import admin

from ecomerc.models import Factory, Retail, Individual
from products.models import Product
from users.models import User


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу заводов """
    list_display = ['id', 'user_name', 'user_email', 'product_list', 'created_at']

    # TODO: сделать выборку user клиентов только Завод
    # TODO: добавить отображение дополнительного поля self.user.name что бы выводилось название пользователя

    def get_readonly_fields(self, request, obj=None):
        """ Делаем поля только для чтения, если просмотр """
        if obj:
            return self.readonly_fields + ('user',)
        return self.readonly_fields

    @admin.display(description='Название завода')
    def user_name(self, product: Product):
        """ Выводим наименование Завода """
        return product.user.name

    @admin.display(description='Электронная почта')
    def user_email(self, product: Product):
        """ Выводим почту Завода """
        return product.user.email

    @admin.display(description='Список товаров')
    def product_list(self, product: Product):
        """ Выводим список продуктов конкретного завода """
        if product:
            products = Product.objects.filter(user=product.user)
            products_name = []
            for product in products:
                products_name.append(product.name)
            return products_name
        return 'Нет продуктов'


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу розничных сетей """
    list_display = ['id', 'user', 'product', 'created_at', 'supplier', 'debt']
    exclude = ['product']
    readonly_fields = ['debt']

    def get_readonly_fields(self, request, obj=None):
        """ Делаем поля только для чтения, если просмотр """
        if obj:
            return self.readonly_fields + ['user', 'supplier']
        return self.readonly_fields

    # TODO: сделать выборку user клиентов только Розничная сеть
    # TODO: добавить отображение дополнительного поля self.user.name


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу индивидуальных предпринимателей """
    list_display = ['id', 'user', 'product', 'created_at', 'supplier', 'debt']
    exclude = ['product']
    readonly_fields = ['debt']

    def get_readonly_fields(self, request, obj=None):
        """ Делаем поля только для чтения, если просмотр """
        if obj:
            return self.readonly_fields + ['user', 'supplier']
        return self.readonly_fields

    # TODO: сделать выборку user клиентов только Индивидуальный предприниматель
    # TODO: добавить отображение дополнительного поля self.user.name



