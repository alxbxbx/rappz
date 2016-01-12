# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 10, 30, 21, 5, 9, 74000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
