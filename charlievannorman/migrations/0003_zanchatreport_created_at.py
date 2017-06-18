# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zannorman', '0002_remove_zanchatreport_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='zanchatreport',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
