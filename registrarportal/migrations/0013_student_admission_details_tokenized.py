# Generated by Django 4.1.2 on 2023-03-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrarportal', '0012_alter_enrollment_batch_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_admission_details',
            name='tokenized',
            field=models.BooleanField(default=False),
        ),
    ]
