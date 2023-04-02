
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studentportal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentrequest',
            name='request_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='documentRequestedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='documentrequest',
            unique_together={('document', 'scheduled_date')},
        ),
    ]
