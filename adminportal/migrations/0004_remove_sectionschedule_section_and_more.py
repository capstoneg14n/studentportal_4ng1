# Generated by Django 4.1.2 on 2023-02-12 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0003_auto_20230212_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionschedule',
            name='section',
        ),
        migrations.RemoveField(
            model_name='sectionschedule',
            name='subject',
        ),
        migrations.DeleteModel(
            name='schoolSections',
        ),
        migrations.DeleteModel(
            name='sectionSchedule',
        ),
    ]