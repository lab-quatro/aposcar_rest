# Generated by Django 3.1.2 on 2020-12-18 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201218_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nominee',
            old_name='picture_cover',
            new_name='picture_url',
        ),
        migrations.RemoveField(
            model_name='nominee',
            name='picture_thumbnail',
        ),
    ]