# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0005_camp_campuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_date',
            field=models.IntegerField(),
        ),
    ]
