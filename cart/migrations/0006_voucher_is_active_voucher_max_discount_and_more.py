# Generated by Django 4.1.7 on 2023-03-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_voucher_voucher_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='voucher',
            name='max_discount',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='voucher',
            name='min_value',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]