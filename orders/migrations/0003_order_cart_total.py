# Generated by Django 2.0.3 on 2018-04-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180428_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
