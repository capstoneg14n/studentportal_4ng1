

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminportal', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='documentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_date', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_cancelledByRegistrar', models.BooleanField(default=False)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='documentRequestDetails', to='adminportal.studentdocument')),
            ],
            options={
                'ordering': ['scheduled_date', 'last_modified'],
            },
        ),
    ]
