# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0005_song_pic_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='date',
            new_name='dateCreated',
        ),
    ]
