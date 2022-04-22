# Generated by Django 3.2.7 on 2022-03-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0029_auto_20220329_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_location_consaltancy',
            fields=[
                ('doctor_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fees', models.CharField(blank=True, default='', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_video_consaltancy',
            fields=[
                ('doctor_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fees', models.CharField(blank=True, default='', max_length=1000, null=True)),
            ],
        ),
    ]
