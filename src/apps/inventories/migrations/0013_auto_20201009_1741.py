# Generated by Django 3.0.10 on 2020-10-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0012_auto_20201008_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True),
        ),
    ]
