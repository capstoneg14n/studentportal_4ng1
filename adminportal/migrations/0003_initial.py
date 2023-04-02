

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminportal', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_email',
            name='email_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_email', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='school_contact_number',
            name='contactnum_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_number', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='firstsemschedule',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='firstSemSched', to='adminportal.schoolsections'),
        ),
        migrations.AddField(
            model_name='firstsemschedule',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='firstSemSubjectSchedule', to='adminportal.subjects'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='g11_firstSem_subjects',
            field=models.ManyToManyField(related_name='grade11_firstSem', to='adminportal.subjects'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='g11_secondSem_subjects',
            field=models.ManyToManyField(related_name='grade11_secondSem', to='adminportal.subjects'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='g12_firstSem_subjects',
            field=models.ManyToManyField(related_name='grade12_firstSem', to='adminportal.subjects'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='g12_secondSem_subjects',
            field=models.ManyToManyField(related_name='grade12_secondSem', to='adminportal.subjects'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='strand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='curriculum_strand', to='adminportal.shs_strand'),
        ),
        migrations.AlterUniqueTogether(
            name='schoolsections',
            unique_together={('sy', 'name')},
        ),
    ]
