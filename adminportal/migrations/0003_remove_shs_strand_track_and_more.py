# Generated by Django 4.1.2 on 2022-11-10 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0002_alter_student_enrollment_details_report_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shs_strand',
            name='track',
        ),
        migrations.RemoveField(
            model_name='student_admission_details',
            name='admission_owner',
        ),
        migrations.RemoveField(
            model_name='student_admission_details',
            name='admission_sy',
        ),
        migrations.RemoveField(
            model_name='student_admission_details',
            name='first_chosen_strand',
        ),
        migrations.RemoveField(
            model_name='student_admission_details',
            name='second_chosen_strand',
        ),
        migrations.RemoveField(
            model_name='student_enrollment_details',
            name='admission_details',
        ),
        migrations.RemoveField(
            model_name='student_enrollment_details',
            name='enrolled_schoolyear',
        ),
        migrations.RemoveField(
            model_name='student_enrollment_details',
            name='selected_strand',
        ),
        migrations.RemoveField(
            model_name='student_enrollment_details',
            name='student_user',
        ),
        migrations.DeleteModel(
            name='school_year',
        ),
        migrations.DeleteModel(
            name='shs_strand',
        ),
        migrations.DeleteModel(
            name='shs_track',
        ),
        migrations.DeleteModel(
            name='student_admission_details',
        ),
        migrations.DeleteModel(
            name='student_enrollment_details',
        ),
    ]