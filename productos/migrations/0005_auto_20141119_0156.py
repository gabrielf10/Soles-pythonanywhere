# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20141119_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='url',
            field=models.ImageField(upload_to=b'img', verbose_name=b'Im\xc3\xa1gen'),
            preserve_default=True,
        ),
    ]
