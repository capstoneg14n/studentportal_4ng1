# Generated by Django 4.1.2 on 2022-12-11 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0004_school_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captured_imgs', models.ImageField(upload_to='Event_pictures/%Y')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('is_hidden', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_photo', to='adminportal.school_events')),
            ],
        ),
    ]
