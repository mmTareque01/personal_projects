# Generated by Django 4.2.4 on 2023-08-28 16:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_users_picture'),
        ('products', '0005_brand_products_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_Products',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('meta_data', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('products', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cart.cart_products')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
