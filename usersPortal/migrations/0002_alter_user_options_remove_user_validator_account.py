# Generated by Django 4.1.2 on 2023-04-06 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RemoveField(
            model_name='user',
            name='validator_account',
        ),
    ]