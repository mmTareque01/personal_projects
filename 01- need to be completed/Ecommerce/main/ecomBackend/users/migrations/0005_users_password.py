# Generated by Django 4.2.4 on 2023-10-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_users_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]