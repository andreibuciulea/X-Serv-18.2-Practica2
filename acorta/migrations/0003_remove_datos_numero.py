# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0002_datos_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datos',
            name='numero',
        ),
    ]
