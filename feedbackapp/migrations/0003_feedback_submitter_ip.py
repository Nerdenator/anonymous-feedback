# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0002_remove_feedback_submitter_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='submitter_ip',
            field=models.GenericIPAddressField(default='127.0.0.1'),
            preserve_default=False,
        ),
    ]
