from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Модель для авторизации """
    username = None

    email = models.EmailField(max_length=255, unique=True, verbose_name='Почта', help_text='Укажите почту')
    user_type = models.OneToOneField('ClientType', on_delete=models.SET_NULL, to_fields='client_type', verbose_name='Тип клиента', related_name='user_type')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ClientType(models.Model):
    """ Модель с типом клиента Завод, оптовик, покупатель """
    CHOICES = {
        "FACTORY": "Factory",
        "RETAIL": "Retail",
        "INDIVIDUAL": "Individual entrepreneur"
    }
    client_type = models.CharField(max_length=15, choices=CHOICES, unique=True, verbose_name='Тип клиента', help_text='Укажите тип клиента')
