# Generated by Django 3.2.17 on 2023-02-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='max_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='min_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
