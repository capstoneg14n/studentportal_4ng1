# Generated by Django 4.1.2 on 2023-03-02 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrarportal', '0011_enrollment_batch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enrollment_batch',
            options={'ordering': ['created_on']},
        ),
    ]
