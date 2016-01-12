# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0002_song_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
