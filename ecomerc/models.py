from django.db import models
from config import settings
from users.models import User

NULLABLE = {"null": True, "blank": True}

class Factory(models.Model):
    """ Модель для таблицы Завод """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', help_text='Выберите пользователя', related_name='user_factory')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, verbose_name='Продукты', **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        return self.user.name

class Retail(models.Model):
    """ Модель для таблицы Розничная сеть """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', help_text='Выберите пользователя', related_name='user_retail')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, verbose_name='Продукты', **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    supplier = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Поставщик', help_text='Укажите поставщика', null=True)
    debt = models.FloatField(default=0, verbose_name='Задолженность перед поставщиком')

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        return self.user.name


class Individual(models.Model):
    """ Модель для таблицы Производителей """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', help_text='Выберите пользователя', related_name='user_individual')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, verbose_name='Продукты', **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    supplier = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Поставщик', help_text='Укажите поставщика', null=True)
    debt = models.FloatField(default=0, verbose_name='Задолженность перед поставщиком')

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

    def __str__(self):
        return self.user.name


class Product(models.Model):
    """ Модель для таблицы Продуктов """
    name = models.CharField(max_length=255, verbose_name='Название', help_text='Укажите название продукта', )
    model_product = models.CharField(max_length=255, verbose_name='Модель', help_text='Укажите модель продукта', **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Добавьте описание продукта', **NULLABLE)
    price = models.FloatField(verbose_name='Цена', help_text='Укажите стоимость', default=0)
    is_published = models.BooleanField(verbose_name='В продаже', help_text='Отметьте если в продаже', default=True)
    release_date = models.DateField(verbose_name='Дата выхода', help_text='Укажите дату выхода на рынок', **NULLABLE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
