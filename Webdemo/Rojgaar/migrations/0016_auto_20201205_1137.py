# Generated by Django 3.1.3 on 2020-12-05 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rojgaar', '0015_auto_20201204_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lrecruiter',
            old_name='jrmobno',
            new_name='rmobno',
        ),
        migrations.RenameField(
            model_name='srecruiter',
            old_name='jrmobno',
            new_name='rmobno',
        ),
    ]