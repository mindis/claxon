# Generated by Django 2.1 on 2018-09-05 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actcode', '0005_auto_20180905_1403'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='annotation',
            unique_together={('document', 'label')},
        ),
    ]
