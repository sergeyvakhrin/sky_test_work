from django.contrib import admin

from ecomerc.models import Factory, Retail, Individual
from users.models import User, ClientType


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу пользователей """
    list_display = ['id','name', 'email', 'country', 'city', 'street', 'house_number', 'user_type']
    list_display_links = ['id','name', 'email', 'country', 'city', 'street', 'house_number', 'user_type']
    exclude = ['last_name', 'first_name']

    def get_readonly_fields(self, request, obj=None):
        """ Делаем поля только для чтения, если просмотр """
        if obj:
            return self.readonly_fields + ('user_type', 'user_supplier', )
        return self.readonly_fields

    @admin.display(description='Поставщик')
    def user_supplier(self, user_by: User):
        """ Выводим наименование Поставщика """
        if user_by.user_type.client_type == 'RETAIL':
            retail = Retail.objects.get(user=user_by)
            return retail.supplier.name
        elif user_by.user_type.client_type == 'INDIVIDUAL':
            individual = Individual.objects.get(user=user_by)
            return individual.supplier.name


@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу тип клиента """
    list_display = ['id', 'client_type']
    list_display_links = ['id', 'client_type']

    def get_readonly_fields(self, request, obj=None):
        """ Делаем поля только для чтения, если просмотр """
        if obj:
            return self.readonly_fields + ('client_type',)
        return self.readonly_fields
