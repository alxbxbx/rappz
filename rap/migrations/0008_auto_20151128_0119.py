# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0007_auto_20151127_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=1000)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RapUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('fb_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='rap_user',
            field=models.ForeignKey(to='rap.RapUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='song',
            field=models.ForeignKey(to='rap.Song'),
        ),
    ]
