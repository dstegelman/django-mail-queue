# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailqueue', '0004_mailermessage_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailermessage',
            name='cc_address',
            field=models.TextField(verbose_name='CC', blank=True),
            preserve_default=True,
        ),
    ]
