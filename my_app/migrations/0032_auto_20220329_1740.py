# Generated by Django 3.2.7 on 2022-03-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0031_doctor_location_consaltancy_location_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_location_consaltancie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('location_id', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('fees', models.CharField(blank=True, default='', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_video_consaltancie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('fees', models.CharField(blank=True, default='', max_length=1000, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Doctor_location_consaltancy',
        ),
        migrations.DeleteModel(
            name='Doctor_video_consaltancy',
        ),
    ]
