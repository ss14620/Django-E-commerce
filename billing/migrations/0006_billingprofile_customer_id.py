# Generated by Django 2.0.3 on 2018-05-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_remove_billingprofile_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingprofile',
            name='customer_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]