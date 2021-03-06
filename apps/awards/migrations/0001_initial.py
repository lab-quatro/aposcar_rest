# Generated by Django 3.1.5 on 2021-01-09 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Nominee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('picture_url', models.ImageField(upload_to='nominees/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'nominees',
            },
        ),
        migrations.CreateModel(
            name='Indication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('annotation', models.TextField()),
                ('is_winner', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.category')),
                ('nominated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.nominee')),
            ],
        ),
    ]
