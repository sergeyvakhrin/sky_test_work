from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}

class User(AbstractUser):
    """ Модель для авторизации """
    username = None

    email = models.EmailField(max_length=255, unique=True, verbose_name='Почта', help_text='Укажите почту')
    user_type = models.OneToOneField('ClientType', on_delete=models.SET_NULL, to_field='client_type', verbose_name='Тип клиента', related_name='user_type', null=True)
    country = models.CharField(max_length=30, verbose_name='Страна', help_text='Укажите страну производства')
    city = models.CharField(max_length=100, verbose_name='Город', help_text='Укажите город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', help_text='Укажите улицу', **NULLABLE)
    house_number = models.CharField(max_length=10, verbose_name='Номер дома', help_text='Укажите номер дома', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class ClientType(models.Model):
    """ Модель с типом клиента Завод, оптовик, покупатель """
    CHOICES = {
        "FACTORY": "Factory",
        "RETAIL": "Retail",
        "INDIVIDUAL": "Individual entrepreneur"
    }
    client_type = models.CharField(max_length=100, choices=CHOICES, unique=True, verbose_name='Тип клиента', help_text='Укажите тип клиента')

    class Meta:
        verbose_name = 'Тип пользователя'
        verbose_name_plural = 'Типы пользователей'

    def __str__(self):
        return self.client_type