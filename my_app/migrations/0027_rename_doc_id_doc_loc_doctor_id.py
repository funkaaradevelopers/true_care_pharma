# Generated by Django 3.2.7 on 2022-03-29 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0026_doc_loc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doc_loc',
            old_name='doc_id',
            new_name='doctor_id',
        ),
    ]
