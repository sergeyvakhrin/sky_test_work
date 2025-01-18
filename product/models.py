from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}

class Product(models.Model):
    """ Модель для таблицы Продуктов """
    name = models.CharField(max_length=255, verbose_name='Название', help_text='Укажите название продукта', )
    model_product = models.CharField(max_length=255, verbose_name='Модель', help_text='Укажите модель продукта', **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Добавьте описание продукта', **NULLABLE)
    price = models.FloatField(verbose_name='Цена', help_text='Укажите стоимость', default=0)
    is_published = models.BooleanField(verbose_name='В продаже', help_text='Отметьте если в продаже', default=True)
    release_date = models.DateField(verbose_name='Дата выхода', help_text='Укажите дату выхода на рынок', **NULLABLE)
    supplier = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Поставщик', help_text='Укажите поставщика', null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
