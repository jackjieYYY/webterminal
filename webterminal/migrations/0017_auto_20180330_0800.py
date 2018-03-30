# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-30 08:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webterminal', '0016_auto_20180329_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='key',
            field=models.TextField(blank=True, verbose_name=b'\xe9\x94\xae'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='method',
            field=models.CharField(choices=[(b'password', b'\xe5\xaf\x86\xe7\xa0\x81'), (b'key', b'key')], default=b'password', max_length=40, verbose_name=b'Method'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='password',
            field=models.CharField(blank=True, max_length=40, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81'),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7'),
        ),
    ]
