# Generated by Django 3.1.2 on 2020-11-02 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201030_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
