# Generated by Django 3.2.7 on 2022-04-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0057_medical_condition_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='primary_member',
            field=models.BooleanField(default=False),
        ),
    ]