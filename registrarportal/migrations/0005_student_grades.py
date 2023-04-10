# Generated by Django 4.1.2 on 2023-04-10 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminportal', '0005_remove_secondsemschedule_namo'),
        ('registrarportal', '0004_delete_student_grades'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.CharField(choices=[('1_Q', 'First Quarter'), ('2_Q', 'Second Quarter'), ('3_Q', 'Third Quarter'), ('4_Q', 'Fourth Quarter')], max_length=3)),
                ('yearLevel', models.CharField(choices=[('11', 'Grade 11'), ('12', 'Grade 12')], max_length=2)),
                ('grade', models.IntegerField()),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='grades', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='subject_grades', to='adminportal.subjects')),
            ],
        ),
    ]
