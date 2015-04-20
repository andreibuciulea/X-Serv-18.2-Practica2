# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos',
            name='numero',
            field=models.PositiveIntegerField(default=15032013),
            preserve_default=False,
        ),
    ]
