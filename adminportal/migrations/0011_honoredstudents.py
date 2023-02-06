# Generated by Django 4.1.2 on 2023-02-06 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0010_auto_20230205_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='honoredStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('honor', models.CharField(choices=[('h', 'With Honor'), ('hh', 'With High Honor'), ('hsh', 'With Highest Honor')], max_length=3, null=True)),
                ('gradPic', models.ImageField(upload_to='graduationPictures')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]