# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-12-16 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_clubs', '__first__'),
        ('gym_contents', '0006_auto_20151216_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='club',
            field=models.ManyToManyField(to='gym_clubs.Club'),
        ),
        migrations.AddField(
            model_name='evento',
            name='club',
            field=models.ManyToManyField(to='gym_clubs.Club'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='club',
            field=models.ManyToManyField(to='gym_clubs.Club'),
        ),
        migrations.AddField(
            model_name='notizia',
            name='club',
            field=models.ManyToManyField(to='gym_clubs.Club'),
        ),
        migrations.AddField(
            model_name='press',
            name='club',
            field=models.ManyToManyField(to='gym_clubs.Club'),
        ),
        migrations.AddField(
            model_name='video',
            name='club',
            field=models.ManyToManyField(to='gym_clubs.Club'),
        ),
    ]
