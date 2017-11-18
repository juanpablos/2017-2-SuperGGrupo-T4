# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-18 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='days_in_adoption',
        ),
        migrations.AddField(
            model_name='animal',
            name='admission_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]