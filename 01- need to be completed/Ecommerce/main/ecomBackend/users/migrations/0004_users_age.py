# Generated by Django 4.2.4 on 2023-10-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='age',
            field=models.IntegerField(default=1, verbose_name=20),
            preserve_default=False,
        ),
    ]
