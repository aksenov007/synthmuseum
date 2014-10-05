# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SynthMuseum', '0003_auto_20141004_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterpole',
            name='type',
            field=models.PositiveSmallIntegerField(unique=True, choices=[(6, '1-pole/6dB per octave'), (12, '2-pole/12dB per octave'), (18, '3-pole/18dB per octave'), (24, '4-pole/24dB per octave')]),
        ),
    ]
