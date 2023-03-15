# Generated by Django 4.1.7 on 2023-03-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20230227_1752'),
        ('orders', '0004_remove_payments_payment_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='variant',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='variant',
            field=models.ManyToManyField(null=True, to='products.variant'),
        ),
    ]
