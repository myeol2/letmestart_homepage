# Generated by Django 2.1 on 2018-09-07 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20180907_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gala',
            name='idx',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='갈라쇼 회차'),
        ),
        migrations.AlterField(
            model_name='play',
            name='idx',
            field=models.PositiveIntegerField(default=1, unique=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='정기공연 회차'),
        ),
    ]
