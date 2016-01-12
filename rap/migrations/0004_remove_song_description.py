# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0003_auto_20151030_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='description',
        ),
    ]
