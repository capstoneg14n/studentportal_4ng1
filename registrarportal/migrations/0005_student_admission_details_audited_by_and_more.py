# Generated by Django 4.1.2 on 2023-04-28 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registrarportal', '0004_alter_dual_citizen_documents_dual_citizenship_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_admission_details',
            name='audited_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='audited_admission', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student_admission_details',
            name='student_lrn',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
