# Generated by Django 4.1.2 on 2023-02-28 23:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0004_auto_20230226_1840'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registrarportal', '0003_student_admission_details_with_enrollment'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_enrollment_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_denied', models.BooleanField(default=False)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('admission', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='enrollment', to='registrarportal.student_admission_details')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='stud_enrollment', to=settings.AUTH_USER_MODEL)),
                ('enrolled_school_year', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sy_enrollee', to='registrarportal.schoolyear')),
                ('strand', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='strand_enrollment', to='adminportal.shs_strand')),
            ],
            options={
                'ordering': ['-enrolled_school_year__id', 'created_on'],
            },
        ),
        migrations.CreateModel(
            name='student_report_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_card', models.ImageField(upload_to='enrollment/report_cards/%Y')),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('card_from', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='report_card', to='registrarportal.student_enrollment_details')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='student_id_picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(upload_to='enrollment/user_pic/%Y')),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image_from', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='stud_pict', to='registrarportal.student_enrollment_details')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='student_home_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permanent_home_address', models.CharField(max_length=50)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('home_of', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='student_contact_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellphone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(regex='^(09)([0-9]{9})$')])),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('own_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user_contact', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
