# Generated by Django 3.1.1 on 2020-09-14 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outlet', models.CharField(max_length=20)),
                ('link', models.URLField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.movie')),
            ],
            options={
                'verbose_name_plural': 'dogs',
            },
        ),
    ]