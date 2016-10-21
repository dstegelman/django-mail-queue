# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailqueue', '0003_auto_20160920_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailermessage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created', null=True),
        ),
    ]
