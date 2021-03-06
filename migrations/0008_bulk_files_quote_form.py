# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import sp3d_quotation.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0007_auto_20170904_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulk_Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(storage=sp3d_quotation.storage_backends.PrivateMediaStorage(), upload_to='bulk_files/')),
            ],
        ),
        migrations.CreateModel(
            name='Quote_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('id_bulk_files', models.CharField(default='', max_length=200)),
                ('quantity', models.IntegerField(default=1)),
                ('email', models.CharField(default='', max_length=200)),
                ('process', models.CharField(default='', max_length=200)),
                ('timeline', models.CharField(default='', max_length=100)),
                ('details', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
