# Generated by Django 4.2.4 on 2023-08-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_brand_products_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]