# Generated by Django 4.0.2 on 2022-02-15 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_leader_username_group_leader_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='main_app.Profile'),
        ),
    ]
