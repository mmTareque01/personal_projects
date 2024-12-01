# Generated by Django 4.2.4 on 2023-10-12 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_products_stock'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.DeleteModel(
            name='Cart_Products',
        ),
    ]