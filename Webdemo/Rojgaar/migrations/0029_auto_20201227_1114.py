# Generated by Django 3.1.3 on 2020-12-27 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rojgaar', '0028_auto_20201225_2218'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostaJob',
            new_name='PosJob',
        ),
        migrations.AlterModelTable(
            name='lrecruiter',
            table=None,
        ),
    ]
