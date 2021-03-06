# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-23 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20180723_1713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(help_text='Подробное описание проекта', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(help_text='Название проекта, отображаемое при открытии', max_length=255, verbose_name='Заголовок'),
        ),
    ]
