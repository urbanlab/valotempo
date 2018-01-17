# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-17 14:57
from __future__ import unicode_literals

import animation.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('p', 'Published'), ('w', 'Withdrawn')], default='p', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Binary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to=animation.models.upload_directory_path_binary)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ligne', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('p', 'Published'), ('w', 'Withdrawn')], default='p', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='GroupBus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('p', 'Published'), ('w', 'Withdrawn')], default='p', max_length=1)),
                ('animation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Animation', to='animation.Animation')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to=animation.models.upload_directory_path_media)),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Groupe', to='animation.GroupBus'),
        ),
        migrations.AddField(
            model_name='animation',
            name='binary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='animation.Binary'),
        ),
        migrations.AddField(
            model_name='animation',
            name='medias',
            field=models.ManyToManyField(to='animation.Media'),
        ),
    ]
