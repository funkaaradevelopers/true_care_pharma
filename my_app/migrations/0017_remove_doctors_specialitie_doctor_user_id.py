# Generated by Django 3.2.7 on 2022-03-24 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0016_rename_doctors_speciality_doctors_specialitie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors_specialitie',
            name='doctor_user_id',
        ),
    ]
