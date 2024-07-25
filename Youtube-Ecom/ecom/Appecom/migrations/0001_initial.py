# Generated by Django 5.0.4 on 2024-07-19 13:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=150)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=7),
                ),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="ProductImage")),
                ("is_sale", models.BooleanField(default=False)),
                (
                    "sale_price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=7),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Appecom.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profil",
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
                ("phone", models.CharField(max_length=10)),
                ("password", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("quantity", models.IntegerField(default=1)),
                ("address", models.TextField()),
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Appecom.product",
                    ),
                ),
                (
                    "profil",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Appecom.profil"
                    ),
                ),
            ],
        ),
    ]
