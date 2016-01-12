# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0004_remove_song_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='pic_url',
            field=models.CharField(default='Http', max_length=100),
            preserve_default=False,
        ),
    ]
