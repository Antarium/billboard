# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='ad_preview',
            field=models.CharField(default=b'', max_length=80, null=True, blank=True),
        ),
    ]
