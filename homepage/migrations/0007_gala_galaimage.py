# Generated by Django 2.1 on 2018-09-07 10:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20180905_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='갈라쇼 회차')),
                ('poster', models.ImageField(upload_to=homepage.models.gala_poster_path, verbose_name='갈라쇼 포스터')),
            ],
        ),
        migrations.CreateModel(
            name='GalaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=homepage.models.gala_media_path, verbose_name='셋리스트')),
                ('gala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='setlists', to='homepage.Gala')),
            ],
        ),
    ]
