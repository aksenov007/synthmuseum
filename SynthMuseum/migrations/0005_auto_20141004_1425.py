# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('SynthMuseum', '0004_auto_20141004_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardsynthesizer',
            name='built_in_speaker_power',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='synthesizer',
            name='rating_user',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
