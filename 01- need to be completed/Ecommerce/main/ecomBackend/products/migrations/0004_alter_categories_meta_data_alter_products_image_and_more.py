# Generated by Django 4.2.4 on 2023-08-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='meta_data',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='meta_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]