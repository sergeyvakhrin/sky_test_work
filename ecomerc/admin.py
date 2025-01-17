from django.contrib import admin

from ecomerc.models import Factory, Retail, Individual, Product


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу заводов """
    list_display = ['id', 'user', 'product', 'created_at']

    # TODO: сделать выборку user клиентов только Завод
    # TODO: добавить отображение дополнительного поля self.user.name


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу розничных сетей """
    list_display = ['id', 'user', 'product', 'created_at', 'supplier', 'debt']

    # TODO: сделать выборку user клиентов только Розничная сеть
    # TODO: добавить отображение дополнительного поля self.user.name


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу индивидуальных предпринимателей """
    list_display = ['id', 'user', 'product', 'created_at', 'supplier', 'debt']

    # TODO: сделать выборку user клиентов только Индивидуальный предприниматель
    # TODO: добавить отображение дополнительного поля self.user.name


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу индивидуальных предпринимателей """
    list_display = ['id', 'name', 'model_product', 'release_date']
