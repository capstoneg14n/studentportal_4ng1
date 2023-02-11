# Generated by Django 4.1.2 on 2023-02-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0019_curriculum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='g11_1q_subjects',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='g11_2q_subjects',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='g11_3q_subjects',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='g11_4q_subjects',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='g12_1q_subjects',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='g12_2q_subjects',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='g12_3q_subjects',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='g12_4q_subjects',
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
    ]
