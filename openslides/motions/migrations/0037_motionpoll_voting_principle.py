# Generated by Django 2.2.14 on 2020-07-31 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motions', '0036_rename_verbose_poll_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='motionpoll',
            name='voting_principle',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
