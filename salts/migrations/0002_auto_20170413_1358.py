# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-13 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinedeploymodel',
            name='audit_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='onlinedeploymodel',
            name='auditor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='onlinedeploymodel',
            name='publish_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='onlinedeploymodel',
            name='publisher',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='onlinedeploymodel',
            name='sql_name',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
