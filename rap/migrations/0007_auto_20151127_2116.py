# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0006_auto_20151105_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='dateCreated',
            new_name='date_created',
        ),
    ]
