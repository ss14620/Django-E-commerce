# Generated by Django 2.0.3 on 2018-04-29 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180429_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='billing_profle',
            new_name='billing_profile',
        ),
    ]
