import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_date', models.DateField()),
            ],
            options={
                'ordering': ['-effective_date'],
            },
            managers=[
                ('allObjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='firstSemSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.TimeField(null=True)),
                ('time_out', models.TimeField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['time_in'],
            },
        ),
        migrations.CreateModel(
            name='school_contact_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellphone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(regex='^(09)([0-9]{9})$')])),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='school_email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='school_events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_on', models.DateField()),
                ('is_cancelled', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['start_on', 'name'],
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='schoolSections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('yearLevel', models.CharField(choices=[('11', 'Grade 11'), ('12', 'Grade 12')], max_length=7)),
                ('allowedPopulation', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='shs_track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=50, unique=True)),
                ('definition', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='studentDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentName', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['documentName', '-date_created', '-last_modified'],
            },
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_remove', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['title', '-created_on'],
                'unique_together': {('code', 'title')},
            },
        ),
        migrations.CreateModel(
            name='shs_strand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strand_name', models.CharField(max_length=5, unique=True)),
                ('definition', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='track_strand', to='adminportal.shs_track')),
            ],
        ),
        migrations.CreateModel(
            name='secondSemSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.TimeField(null=True)),
                ('namo', models.CharField(max_length=20, null=True)),
                ('time_out', models.TimeField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='secondSemSched', to='adminportal.schoolsections')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='secondSemSubjectSchedule', to='adminportal.subjects')),
            ],
            options={
                'ordering': ['time_in'],
            },
        ),
        migrations.AddField(
            model_name='schoolsections',
            name='assignedStrand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='section_strand', to='adminportal.shs_strand'),
        ),
        migrations.AddField(
            model_name='schoolsections',
            name='first_sem_subjects',
            field=models.ManyToManyField(related_name='firstSemSubjects', through='adminportal.firstSemSchedule', to='adminportal.subjects'),
        ),
        migrations.AddField(
            model_name='schoolsections',
            name='second_sem_subjects',
            field=models.ManyToManyField(related_name='secondSemSubjects', through='adminportal.secondSemSchedule', to='adminportal.subjects'),
        ),
    ]
