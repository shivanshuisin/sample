# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0009_auto_20170412_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='current_month',
            field=models.FileField(default='/media/notext.txt', upload_to='/home/shivanshu/Documents/final/media/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='oldest_month',
            field=models.FileField(default='/media/notext.txt', upload_to='/home/shivanshu/Documents/final/media/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='previous_month',
            field=models.FileField(default='/media/notext.txt', upload_to='/home/shivanshu/Documents/final/media/'),
        ),
    ]
