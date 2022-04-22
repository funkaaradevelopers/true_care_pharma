# Generated by Django 3.2.7 on 2022-04-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0035_doctor_location_consaltancie_currency_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('location_id', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('day', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('_from', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('to', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
    ]
