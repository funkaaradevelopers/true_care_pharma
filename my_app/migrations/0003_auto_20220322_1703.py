# Generated by Django 3.2.7 on 2022-03-22 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='date_of_birth',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email_id',
            field=models.EmailField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='password',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
