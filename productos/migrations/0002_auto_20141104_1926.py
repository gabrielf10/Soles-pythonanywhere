# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name_plural': 'Categor\xedas'},
        ),
        migrations.AlterModelOptions(
            name='imagenes',
            options={'verbose_name_plural': 'Im\xe1genes'},
        ),
        migrations.AlterField(
            model_name='imagenes',
            name='categoria_id',
            field=models.ForeignKey(verbose_name=b'Categor\xc3\xada', to='productos.Categoria'),
            preserve_default=True,
        ),
    ]
