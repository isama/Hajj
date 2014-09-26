# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0007_auto_20140925_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 25, 1, 51, 36, 726327), verbose_name=b'End Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 25, 1, 51, 36, 726298), verbose_name=b'Start Date'),
            preserve_default=True,
        ),
    ]
