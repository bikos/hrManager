# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hrTransaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_field', models.CharField(max_length=20, db_column=b'class')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='class_id',
            field=models.ForeignKey(default=datetime.datetime(2015, 12, 27, 21, 22, 45, 260000, tzinfo=utc), to='hrTransaction.ClassName'),
            preserve_default=False,
        ),
    ]
