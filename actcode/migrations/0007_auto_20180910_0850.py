# Generated by Django 2.1 on 2018-09-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actcode', '0006_auto_20180905_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='label',
            name='eval_task',
        ),
        migrations.RemoveField(
            model_name='label',
            name='fn',
        ),
        migrations.RemoveField(
            model_name='label',
            name='fp',
        ),
        migrations.RemoveField(
            model_name='label',
            name='last_eval',
        ),
        migrations.RemoveField(
            model_name='label',
            name='tp',
        ),
        migrations.RemoveField(
            model_name='project',
            name='model_task',
        ),
        migrations.AddField(
            model_name='project',
            name='model_evaluation',
            field=models.TextField(null=True),
        ),
    ]
