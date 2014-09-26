# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Web', '0003_actionhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
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
        migrations.RemoveField(
            model_name='mapping',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='mapping',
            name='user',
        ),
        migrations.DeleteModel(
            name='Mapping',
        ),
    ]
