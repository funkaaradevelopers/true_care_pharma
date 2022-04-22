# Generated by Django 3.2.7 on 2022-03-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0022_auto_20220329_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc_loc',
            fields=[
                ('doc_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('loc_id', models.CharField(blank=True, default='', max_length=30, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctors_location',
            name='doctor_user_id',
        ),
    ]
