# Generated by Django 3.2.7 on 2022-03-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0028_auto_20220329_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor_loccation',
            name='id',
        ),
        migrations.AlterField(
            model_name='doctor_loccation',
            name='loc_id',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False),
        ),
    ]