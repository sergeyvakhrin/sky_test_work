# Generated by Django 5.1.5 on 2025-01-18 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0009_remove_product_user_product_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="warehouse",
            name="name",
        ),
    ]
