# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 06:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Äàòà ïóáëèêàöèè')),
                ('text', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Çàãîëîâîê')),
                ('date', models.DateTimeField(verbose_name='Äàòà ïóáëèêàöèè')),
                ('message', models.TextField(max_length=10000, verbose_name='Òåêñò ñîîáùåíèÿ')),
                ('author', models.CharField(max_length=100, verbose_name='Èìÿ àâòîðà')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]