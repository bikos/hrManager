# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrTransaction', '0002_auto_20151227_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='class_id',
        ),
        migrations.DeleteModel(
            name='ClassName',
        ),
    ]
