# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('publication_date', models.DateTimeField()),
                ('m_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='House.House')),
            ],
        ),
    ]
