# Generated by Django 4.1.2 on 2023-04-28 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrarportal', '0005_student_admission_details_audited_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_admission_details',
            name='student_lrn',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
