# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SynthMuseum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='manufacturer',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='synthesizer',
            name='manufacturer',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='synthesizer',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
