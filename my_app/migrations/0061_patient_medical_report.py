# Generated by Django 3.2.7 on 2022-04-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0060_patient_medical_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_medical_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('report_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('report_image', models.ImageField(upload_to='media-files/patients_report_images')),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
    ]