# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20170615_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoquestion',
            name='question_text',
            field=models.CharField(default=b'Are you interested?', max_length=100),
        ),
        migrations.AlterField(
            model_name='videotag',
            name='title',
            field=models.CharField(default=b'Video Title', max_length=100),
        ),
    ]
