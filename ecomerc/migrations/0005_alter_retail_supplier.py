# Generated by Django 5.1.5 on 2025-01-19 15:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecomerc", "0004_alter_individual_product_alter_retail_product_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="retail",
            name="supplier",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите поставщика",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Поставщик",
            ),
        ),
    ]
