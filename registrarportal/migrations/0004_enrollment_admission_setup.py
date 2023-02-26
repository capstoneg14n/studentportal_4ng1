# Generated by Django 4.1.2 on 2023-02-20 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrarportal', '0003_delete_enrollment_admission_setup'),
    ]

    operations = [
        migrations.CreateModel(
            name='enrollment_admission_setup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('students_perBatch', models.IntegerField()),
                ('acceptResponses', models.BooleanField(default=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('ea_setup_sy', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='e_a_setup', to='registrarportal.schoolyear')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]