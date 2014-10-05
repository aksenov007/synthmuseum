# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SynthMuseum', '0005_auto_20141004_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='synthesizer',
            name='description',
            field=models.TextField(default='Please, enter some description...'),
            preserve_default=True,
        ),
    ]
