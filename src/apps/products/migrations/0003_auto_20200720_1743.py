# Generated by Django 3.0.8 on 2020-07-20 17:43

import apps.products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200707_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Unit'),
        ),
    ]