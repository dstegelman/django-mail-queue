# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailqueue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailermessage',
            name='reply_to',
            field=models.TextField(max_length=250, null=True, verbose_name='Reply to', blank=True),
            preserve_default=True,
        ),
    ]
