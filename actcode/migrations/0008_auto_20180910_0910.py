# Generated by Django 2.1 on 2018-09-10 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actcode', '0007_auto_20180910_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='last_model',
            new_name='model_timestamp',
        ),
    ]