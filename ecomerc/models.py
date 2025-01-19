from django.db import models
from config import settings
from products.models import Product
from users.models import User

NULLABLE = {"null": True, "blank": True}

class Factory(models.Model):
    """ Модель для таблицы Завод """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', help_text='Выберите пользователя', related_name='user_factory')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Продукты', **NULLABLE) # TODO: отобразить список продуктов
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)

    # TODO: Поле user выдавать только клиенты с типом Завод. А лучше автоматически создавать Завод в момент создания пользователя с типом завод

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        return self.user.name

class Retail(models.Model):
    """ Модель для таблицы Розничная сеть """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', help_text='Выберите пользователя', related_name='user_retail')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Продукты', **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    supplier = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Поставщик', help_text='Укажите поставщика', null=True)
    debt = models.FloatField(default=0, verbose_name='Задолженность перед поставщиком')

    # TODO: Поле user выдавать только клиенты с типом Розничная сеть. А лучше автоматически создавать Завод в момент создания пользователя с типом Розничная сеть

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        return self.user.name

    # TODO: добавить проверку: пользователь не может быть сам себе поставщик


class Individual(models.Model):
    """ Модель для таблицы Индивидуальный предприниматель """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', help_text='Выберите пользователя', related_name='user_individual')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Продукты', **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    supplier = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Поставщик', help_text='Укажите поставщика', null=True)
    debt = models.FloatField(default=0, verbose_name='Задолженность перед поставщиком')

    # TODO: Поле user выдавать только клиенты с типом Индивидуальный предприниматель. А лучше автоматически создавать Завод в момент создания пользователя с типом Индивидуальный предприниматель

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

    def __str__(self):
        return self.user.name

    # TODO: добавить проверку: пользователь не может быть сам себе поставщик


# class WarehouseFactory(models.Model):
#     """ Модель доя таблицы склада Завода """
#     name = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='Склад завода', help_text='Укажите Завод')
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Продукт', help_text='Укажите продукт', null=True)
#     price = models.FloatField(default=0, verbose_name='Цена', help_text='Укажите стоимость за шт')
#     quantity = models.IntegerField(default=0, verbose_name='Количество')
#
#     class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = 'Продукты'
#
#     def __str__(self):
#         return self.product.name
#
#
# class WarehouseRetail(models.Model):
#     """ Модель доя таблицы склада Розничная сеть """
#     name = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='Склад завода', help_text='Укажите Завод')
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Продукт', help_text='Укажите продукт', null=True)
#     price = models.FloatField(default=0, verbose_name='Цена', help_text='Укажите стоимость за шт')
#     quantity = models.IntegerField(default=0, verbose_name='Количество')
#
#     class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = 'Продукты'
#
#     def __str__(self):
#         return self.product.name
#
#
# class WarehouseIndividual(models.Model):
#     """ Модель доя таблицы склада Индивидуальный предприниматель """
#     name = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='Склад завода', help_text='Укажите Завод')
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Продукт', help_text='Укажите продукт', null=True)
#     price = models.FloatField(default=0, verbose_name='Цена', help_text='Укажите стоимость за шт')
#     quantity = models.IntegerField(default=0, verbose_name='Количество')
#     purchase_price = models.FloatField(verbose_name='Цена закупки')
#
#     class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = 'Продукты'
#
#     def __str__(self):
#         return self.product.name

