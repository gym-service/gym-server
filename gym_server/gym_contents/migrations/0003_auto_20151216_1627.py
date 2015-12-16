# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-12-16 16:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym_contents', '0002_notizia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordine', models.IntegerField(blank=True, default=0)),
                ('titolo', models.CharField(max_length=80)),
                ('sottotitolo', models.CharField(blank=True, max_length=80, null=True)),
                ('descrizione', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('stato', models.IntegerField(blank=True, choices=[[0, 'Non pubblicato'], [1, 'In prova'], [2, 'Pubblicato']], default=0)),
                ('promosso', models.BooleanField(default=False)),
                ('url', models.URLField(blank=True, null=True)),
                ('immagine', models.ImageField(blank=True, null=True, upload_to='immagini')),
                ('allegato', models.FileField(blank=True, null=True, upload_to='allegati')),
                ('data', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Articolo',
                'verbose_name_plural': 'Articoli',
            },
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventi'},
        ),
        migrations.AlterModelOptions(
            name='notizia',
            options={'verbose_name': 'Notizia', 'verbose_name_plural': 'Notizie'},
        ),
    ]
