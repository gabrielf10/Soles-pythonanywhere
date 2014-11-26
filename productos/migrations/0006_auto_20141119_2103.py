# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20141119_0156'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Imagenes',
            new_name='Imagen',
        ),
        migrations.RenameField(
            model_name='imagen',
            old_name='categoria_id',
            new_name='categoria',
        ),
    ]
