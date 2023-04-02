

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registrarportal', '0001_initial'),
        ('adminportal', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_home_address',
            name='home_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user_address', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student_enrollment_details',
            name='admission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='enrollment', to='registrarportal.student_admission_details'),
        ),
        migrations.AddField(
            model_name='student_enrollment_details',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='stud_enrollment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student_enrollment_details',
            name='enrolled_school_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sy_enrollee', to='registrarportal.schoolyear'),
        ),
        migrations.AddField(
            model_name='student_enrollment_details',
            name='strand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='strand_enrollment', to='adminportal.shs_strand'),
        ),
        migrations.AddField(
            model_name='student_contact_number',
            name='enrollment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='enrollment_contactnumber', to='registrarportal.student_enrollment_details'),
        ),
        migrations.AddField(
            model_name='student_contact_number',
            name='own_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user_contact', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student_admission_details',
            name='admission_owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='admission_details', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student_admission_details',
            name='admission_sy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sy_admitted', to='registrarportal.schoolyear'),
        ),
        migrations.AddField(
            model_name='student_admission_details',
            name='assigned_curriculum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='with_admission', to='adminportal.curriculum'),
        ),
        migrations.AddField(
            model_name='student_admission_details',
            name='first_chosen_strand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='first_strand', to='adminportal.shs_strand'),
        ),
        migrations.AddField(
            model_name='student_admission_details',
            name='second_chosen_strand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='second_strand', to='adminportal.shs_strand'),
        ),
        migrations.AddField(
            model_name='ph_born',
            name='admission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='softCopy_admissionRequirements_phBorn', to='registrarportal.student_admission_details'),
        ),
        migrations.AddField(
            model_name='foreign_citizen_documents',
            name='admission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='softCopy_admissionRequirements_foreigner', to='registrarportal.student_admission_details'),
        ),
        migrations.AddField(
            model_name='enrollment_invitations',
            name='invitation_to',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='invitation', to='registrarportal.student_admission_details'),
        ),
        migrations.AddField(
            model_name='enrollment_batch',
            name='members',
            field=models.ManyToManyField(related_name='enrollment_batch_member', to='registrarportal.student_enrollment_details'),
        ),
        migrations.AddField(
            model_name='enrollment_batch',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='section_batch', to='adminportal.schoolsections'),
        ),
        migrations.AddField(
            model_name='enrollment_batch',
            name='sy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sy_enrollment_batches', to='registrarportal.schoolyear'),
        ),
        migrations.AddField(
            model_name='enrollment_admission_setup',
            name='ea_setup_sy',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='e_a_setup', to='registrarportal.schoolyear'),
        ),
        migrations.AddField(
            model_name='dual_citizen_documents',
            name='admission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='softCopy_admissionRequirements_dualCitizen', to='registrarportal.student_admission_details'),
        ),
        migrations.AddField(
            model_name='admission_batch',
            name='members',
            field=models.ManyToManyField(related_name='admission_batch_member', to='registrarportal.student_admission_details'),
        ),
        migrations.AddField(
            model_name='admission_batch',
            name='sy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sy_admission_batches', to='registrarportal.schoolyear'),
        ),
        migrations.AlterUniqueTogether(
            name='student_enrollment_details',
            unique_together={('applicant', 'admission', 'enrolled_school_year')},
        ),
    ]
