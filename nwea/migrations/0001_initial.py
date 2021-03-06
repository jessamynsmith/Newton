# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NWEADomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.IntegerField(choices=[(1, 'Operations and Algebraic Thinking'), (2, 'Number and Operations'), (3, 'Measurement and Data'), (4, 'Geometry')], default=1, verbose_name='Domain')),
            ],
            options={
                'verbose_name_plural': 'NWEA Domains',
                'verbose_name': 'NWEA Domain',
            },
        ),
        migrations.CreateModel(
            name='NWEARITBand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rit_band', models.IntegerField(choices=[(111, '111'), (121, '121'), (131, '131'), (141, '141'), (151, '151'), (161, '161'), (171, '171'), (181, '181'), (191, '191'), (201, '201'), (211, '211'), (221, '221'), (231, '231'), (241, '241')], default=151)),
            ],
            options={
                'verbose_name_plural': 'NWEA RIT Bands',
                'verbose_name': 'NWEA RIT Band',
            },
        ),
        migrations.CreateModel(
            name='NWEASubDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_domain', models.IntegerField(choices=[(1, 'Represent and Solve Problems'), (2, 'Properties of Operations'), (3, 'Understand Place Value, Counting, and Cardinality'), (4, 'Number and Operations: Base Ten and Fractions'), (5, 'Solve Problems Involving Measurement'), (6, 'Represent and Interpret Data'), (7, 'Reason with Shapes and Their Attributes')], default=1, verbose_name='Sub-Domain')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nwea.NWEADomain', verbose_name='Domain')),
            ],
            options={
                'verbose_name_plural': 'NWEA Sub-Domains',
                'verbose_name': 'NWEA Sub-Domain',
            },
        ),
        migrations.CreateModel(
            name='NWEATestResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='nwearitband',
            name='sub_domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nwea.NWEASubDomain'),
        ),
    ]
