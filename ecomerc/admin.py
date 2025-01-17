from django.contrib import admin

from ecomerc.models import Factory, Retail, Individual


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу заводов """
    list_display = '__all__'


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу розничных сетей """
    list_display = '__all__'


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу индивидуальных предпринимателей """
    list_display = '__all__'
