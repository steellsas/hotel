# Generated by Django 3.1.7 on 2021-03-14 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20210314_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='properties',
            new_name='properties1',
        ),
    ]