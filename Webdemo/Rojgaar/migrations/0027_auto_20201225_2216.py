# Generated by Django 3.1.3 on 2020-12-25 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rojgaar', '0026_auto_20201225_2208'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RPostJob',
            new_name='PostJob',
        ),
        migrations.AlterModelTable(
            name='postjob',
            table='rojgaar_postjob',
        ),
    ]