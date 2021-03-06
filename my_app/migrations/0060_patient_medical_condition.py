# Generated by Django 3.2.7 on 2022-04-15 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0059_customer_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_medical_condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('condition_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('since_how_long', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('medicine', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
    ]
