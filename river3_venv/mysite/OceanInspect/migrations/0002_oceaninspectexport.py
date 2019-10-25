# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OceanInspect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OceanInspectExport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('TestName', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
