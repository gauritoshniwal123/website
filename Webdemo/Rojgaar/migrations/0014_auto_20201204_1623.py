# Generated by Django 3.1.3 on 2020-12-04 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rojgaar', '0013_auto_20201204_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ljobseeker',
            old_name='rmobno',
            new_name='jrmobno',
        ),
        migrations.RenameField(
            model_name='lrecruiter',
            old_name='rmobno',
            new_name='jrmobno',
        ),
        migrations.RenameField(
            model_name='sjobseeker',
            old_name='rmobno',
            new_name='jrmobno',
        ),
        migrations.RenameField(
            model_name='srecruiter',
            old_name='rmobno',
            new_name='jrmobno',
        ),
    ]
