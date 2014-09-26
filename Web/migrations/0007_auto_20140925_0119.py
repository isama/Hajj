# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0006_auto_20140925_0114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='end_date',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='start_date',
            new_name='start',
        ),
    ]
