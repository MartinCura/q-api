# Generated by Django 3.0.2 on 2020-05-22 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_friendshiprequest_friendshipstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='user_requested',
        ),
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='user_requesting',
        ),
        migrations.AddField(
            model_name='friendshiprequest',
            name='profile_requested',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile_requested', to='profiles.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friendshiprequest',
            name='profile_requesting',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile_requesting', to='profiles.Profile'),
            preserve_default=False,
        ),
    ]
