# Generated by Django 3.1.2 on 2020-11-15 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GGcatalogo', '0002_auto_20201115_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desarrollador',
            old_name='fecha_creacion',
            new_name='creacion',
        ),
    ]
