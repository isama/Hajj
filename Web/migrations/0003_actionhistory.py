# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Web', '0002_auto_20140923_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=1000)),
                ('updated_at', models.DateTimeField(verbose_name=b'Updated At')),
                ('activity', models.ForeignKey(to='Web.Activity')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
