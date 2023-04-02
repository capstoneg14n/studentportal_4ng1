

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admission_batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='dual_citizen_documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_moral', models.ImageField(upload_to='admission/goodMorals/%Y')),
                ('report_card', models.ImageField(upload_to='admission/reportCards/%Y')),
                ('psa', models.ImageField(upload_to='admission/studentPsa/%Y')),
                ('dual_citizenship', models.ImageField(upload_to='admission/dualCitizenDocuments/dualCitizenshipCertificates/%Y')),
                ('philippine_passport', models.ImageField(upload_to='admission/dualCitizenDocuments/phPassports/%Y')),
                ('f137', models.ImageField(upload_to='admission/dualCitizenDocuments/f137s/%Y')),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
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
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='enrollment_batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='enrollment_batch_manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='enrollment_invitations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='foreign_citizen_documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_moral', models.ImageField(upload_to='admission/goodMorals/%Y')),
                ('report_card', models.ImageField(upload_to='admission/reportCards/%Y')),
                ('psa', models.ImageField(upload_to='admission/studentPsa/%Y')),
                ('alien_certificate_of_registration', models.ImageField(upload_to='admission/foreignCitizenDocuments/alienRegistration/%Y')),
                ('study_permit', models.ImageField(upload_to='admission/foreignCitizenDocuments/studyPermit/%Y')),
                ('f137', models.ImageField(upload_to='admission/foreignCitizenDocuments/f137s/%Y')),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ph_born',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_moral', models.ImageField(upload_to='admission/goodMorals/%Y')),
                ('report_card', models.ImageField(upload_to='admission/reportCards/%Y')),
                ('psa', models.ImageField(upload_to='admission/studentPsa/%Y')),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='schoolYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_on', models.DateField()),
                ('until', models.DateField()),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='student_admission_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('date_of_birth', models.DateField()),
                ('birthplace', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=50)),
                ('elem_name', models.CharField(max_length=50)),
                ('elem_address', models.CharField(max_length=50)),
                ('elem_region', models.CharField(max_length=30)),
                ('elem_year_completed', models.DateField()),
                ('elem_pept_passer', models.BooleanField(default=False)),
                ('elem_pept_date_completion', models.DateField(blank=True, null=True)),
                ('elem_ae_passer', models.BooleanField(default=False)),
                ('elem_ae_date_completion', models.DateField(blank=True, null=True)),
                ('elem_community_learning_center', models.CharField(blank=True, max_length=50, null=True)),
                ('elem_clc_address', models.CharField(blank=True, max_length=50, null=True)),
                ('jhs_name', models.CharField(max_length=50)),
                ('jhs_address', models.CharField(max_length=50)),
                ('jhs_region', models.CharField(max_length=30)),
                ('jhs_year_completed', models.DateField()),
                ('jhs_pept_passer', models.BooleanField(default=False)),
                ('jhs_pept_date_completion', models.DateField(blank=True, null=True)),
                ('jhs_ae_passer', models.BooleanField(default=False)),
                ('jhs_ae_date_completion', models.DateField(blank=True, null=True)),
                ('jhs_community_learning_center', models.CharField(blank=True, max_length=50, null=True)),
                ('jhs_clc_address', models.CharField(blank=True, max_length=50, null=True)),
                ('is_accepted', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('1', 'Philippine Born'), ('2', 'Foreign Citizen'), ('3', 'Dual Citizen')], max_length=1)),
                ('is_denied', models.BooleanField(default=False)),
                ('with_enrollment', models.BooleanField(default=False)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-admission_sy__id', 'created_on'],
                'get_latest_by': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='student_contact_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellphone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^(09)([0-9]{9})$')])),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='student_enrollment_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_level', models.CharField(choices=[('11', 'Grade 11'), ('12', 'Grade 12')], max_length=7)),
                ('full_name', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_denied', models.BooleanField(default=False)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
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
                ('enrollment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='enrollment_address', to='registrarportal.student_enrollment_details')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
