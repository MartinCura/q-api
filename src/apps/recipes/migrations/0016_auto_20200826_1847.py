# Generated by Django 3.0.9 on 2020-08-26 18:47

import apps.products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_amount_unit'),
        ('recipes', '0015_ingredient_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='amount',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.DecimalField(decimal_places=5, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Unit'),
        ),
    ]
