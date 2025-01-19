from django.contrib import admin

from ecomerc.models import Factory, Retail, Individual
from users.models import User, ClientType


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу пользователей """
    list_display = ['id','name', 'email', 'country', 'city', 'street', 'house_number', 'user_type']
    list_display_links = ['id','name', 'email', 'country', 'city', 'street', 'house_number', 'user_type']

    def get_readonly_fields(self, request, obj=None):
        """ Делаем поля только для чтения, если просмотр """
        if obj:
            return self.readonly_fields + ('user_type',)
        return self.readonly_fields


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
