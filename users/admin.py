from django.contrib import admin

from users.models import User, ClientType


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу пользователей """
    list_display = '__all__'


@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    """ Выводим в админ панель таблицу тип клиента """
    list_display = '__all__'
