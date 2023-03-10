# Generated by Django 3.2.17 on 2023-03-04 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=1000, null=True)),
                ('address2', models.CharField(max_length=1000, null=True)),
                ('address_type', models.CharField(choices=[('Home Address', 'Home Address'), ('Office Address', 'Office Address')], max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('pin_code', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
