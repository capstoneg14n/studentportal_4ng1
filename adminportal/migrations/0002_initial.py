

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminportal', '0001_initial'),
        ('registrarportal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolsections',
            name='sy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sy_section', to='registrarportal.schoolyear'),
        ),
    ]
