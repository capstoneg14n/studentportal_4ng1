# Generated by Django 4.1.2 on 2023-03-04 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrarportal', '0016_enrollment_invitations'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment_invitations',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]