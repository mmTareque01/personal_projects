# Generated by Django 4.2.4 on 2023-10-06 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_products_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(),
        ),
    ]