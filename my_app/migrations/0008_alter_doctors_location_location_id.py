# Generated by Django 3.2.7 on 2022-03-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_auto_20220322_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors_location',
            name='location_id',
            field=models.CharField(default='', max_length=4294967295, primary_key=True, serialize=False),
        ),
    ]
