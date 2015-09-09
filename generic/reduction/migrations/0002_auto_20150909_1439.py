# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reduction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(default=b'NOT_SUBMITED', max_length=30, choices=[(b'NOT_SUBMITED', b'Not Submited'), (b'RUNNING', b'Running'), (b'QUEUED', b'Queued'), (b'COMPLETED', b'Completed'), (b'REMOVED', b'Removed'), (b'DEFERRED', b'Deferred'), (b'IDLE', b'Idle'), (b'UNKNOWN', b'Unknown')]),
        ),
    ]
