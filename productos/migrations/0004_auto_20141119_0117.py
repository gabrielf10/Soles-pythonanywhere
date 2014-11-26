# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20141118_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='url',
            field=models.ImageField(upload_to=b'img', null=True, verbose_name=b'Im\xc3\xa1gen', blank=True),
            preserve_default=True,
        ),
    ]
