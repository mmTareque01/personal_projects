# Generated by Django 4.2.4 on 2023-08-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_address_alter_users_meta_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
