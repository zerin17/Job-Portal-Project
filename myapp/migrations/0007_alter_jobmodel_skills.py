# Generated by Django 5.1.2 on 2024-10-31 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_skills_recruiterprofilemodel_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='skills',
            field=models.CharField(choices=[('programming', 'Programming'), ('networking', 'Networking'), ('hardware', 'Hardware')], max_length=100, null=True),
        ),
    ]