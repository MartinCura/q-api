# Generated by Django 3.0.9 on 2020-09-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_auto_20200827_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishlabel',
            name='image',
            field=models.ImageField(null=True, upload_to='images/dish-labels/%Y-%m-%d'),
        ),
    ]