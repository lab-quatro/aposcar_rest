# Generated by Django 3.1.2 on 2020-12-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_nominee_annotation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nominee',
            name='annotation',
        ),
        migrations.AddField(
            model_name='indication',
            name='annotation',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]