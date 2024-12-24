# Generated by Django 5.1.4 on 2024-12-23 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mpaarating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('label', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img_path', models.TextField()),
                ('duration', models.IntegerField()),
                ('genres', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('user_rating', models.IntegerField()),
                ('mpaa_rating_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.mpaarating')),
            ],
        ),
    ]