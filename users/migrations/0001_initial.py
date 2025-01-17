# Generated by Django 5.1.5 on 2025-01-17 13:14

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClientType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "client_type",
                    models.CharField(
                        choices=[
                            ("FACTORY", "Factory"),
                            ("RETAIL", "Retail"),
                            ("INDIVIDUAL", "Individual entrepreneur"),
                        ],
                        help_text="Укажите тип клиента",
                        max_length=100,
                        unique=True,
                        verbose_name="Тип клиента",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип пользователя",
                "verbose_name_plural": "Типы пользователей",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Укажите почту",
                        max_length=255,
                        unique=True,
                        verbose_name="Почта",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите наименование организации",
                        max_length=255,
                        unique=True,
                        verbose_name="Наименование организации",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        help_text="Укажите страну производства",
                        max_length=30,
                        verbose_name="Страна",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        help_text="Укажите город",
                        max_length=100,
                        null=True,
                        verbose_name="Город",
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True,
                        help_text="Укажите улицу",
                        max_length=100,
                        null=True,
                        verbose_name="Улица",
                    ),
                ),
                (
                    "house_number",
                    models.CharField(
                        blank=True,
                        help_text="Укажите номер дома",
                        max_length=10,
                        null=True,
                        verbose_name="Номер дома",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
                (
                    "user_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_type",
                        to="users.clienttype",
                        to_field="client_type",
                        verbose_name="Тип клиента",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
