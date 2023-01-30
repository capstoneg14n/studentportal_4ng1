# Generated by Django 4.1.2 on 2023-01-31 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminportal', '0003_studentdocument'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='documentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_date', models.DateField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='documentRequestDetails', to='adminportal.studentdocument')),
                ('request_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='documentRequestedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
