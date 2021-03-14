# Generated by Django 3.1.3 on 2020-12-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rojgaar', '0024_delete_postjob'),
    ]

    operations = [
        migrations.CreateModel(
            name='RPostJob',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rmobno', models.CharField(max_length=10)),
                ('jtitle', models.CharField(max_length=30)),
                ('jadd', models.CharField(max_length=100)),
                ('jobtype', models.CharField(default='', editable=False, max_length=50)),
                ('jobcat', models.CharField(default='', editable=False, max_length=100)),
                ('noofopen', models.CharField(max_length=10)),
                ('salary', models.CharField(max_length=10)),
                ('jstime', models.CharField(max_length=10)),
                ('jetime', models.CharField(max_length=10)),
                ('jobdes', models.CharField(max_length=500)),
                ('comname', models.CharField(max_length=100)),
                ('comtagline', models.CharField(max_length=200)),
                ('comdes', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'rojgaar_postjob',
            },
        ),
    ]