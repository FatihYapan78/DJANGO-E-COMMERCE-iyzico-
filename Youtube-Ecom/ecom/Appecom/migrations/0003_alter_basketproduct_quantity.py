# Generated by Django 5.0.4 on 2024-07-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Appecom", "0002_basketproduct"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basketproduct",
            name="quantity",
            field=models.IntegerField(),
        ),
    ]
