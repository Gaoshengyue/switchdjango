# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-02 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.FileField(upload_to='book/')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionBook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_book', to='app.Book')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionMovie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionMusic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.FileField(upload_to='movie/')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.FileField(upload_to='music/')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music', to='app.UserInfo'),
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='app.UserInfo'),
        ),
        migrations.AddField(
            model_name='collectionmusic',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_music', to='app.Music'),
        ),
        migrations.AddField(
            model_name='collectionmusic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_music', to='app.UserInfo'),
        ),
        migrations.AddField(
            model_name='collectionmovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_movie', to='app.Movie'),
        ),
        migrations.AddField(
            model_name='collectionmovie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_movie', to='app.UserInfo'),
        ),
        migrations.AddField(
            model_name='collectionbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_book', to='app.UserInfo'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='app.UserInfo'),
        ),
    ]
