# Generated by Django 3.1.7 on 2021-03-13 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='photo_id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='property_id',
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
