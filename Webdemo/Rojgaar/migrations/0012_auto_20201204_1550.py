# Generated by Django 3.1.3 on 2020-12-04 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rojgaar', '0011_auto_20201204_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lrecruiter',
            old_name='rmobno',
            new_name='lrmobno',
        ),
    ]