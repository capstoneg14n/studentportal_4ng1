# Generated by Django 4.1.2 on 2023-02-25 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrarportal', '0010_admission_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission_batch',
            name='strand',
        ),
    ]
