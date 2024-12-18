# Generated by Django 5.1.2 on 2024-10-31 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_recruiterprofilemodel_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiterprofilemodel',
            name='skills',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='seekerprofilemodel',
            name='skills',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='category',
            field=models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('internship', 'Internship')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='job_title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='number_of_openings',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='skills',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
