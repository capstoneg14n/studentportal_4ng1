# Generated by Django 4.1.2 on 2023-03-02 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrarportal', '0007_enrollment_batch_manager_student_enrollment_details_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='enrollment_batch',
        ),
    ]