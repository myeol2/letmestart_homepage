# Generated by Django 2.1 on 2018-09-05 07:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20180905_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='idx',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='정기공연 회차'),
        ),
        migrations.AlterField(
            model_name='play',
            name='num_of_audience',
            field=models.PositiveIntegerField(default=1, verbose_name='관객 수'),
        ),
        migrations.AlterField(
            model_name='play',
            name='poster',
            field=models.ImageField(upload_to='homepage/static/img', verbose_name='포스터 이미지'),
        ),
        migrations.AlterField(
            model_name='play',
            name='synopsis',
            field=models.TextField(verbose_name='시놉시스'),
        ),
        migrations.AlterField(
            model_name='play',
            name='title',
            field=models.CharField(max_length=50, verbose_name='공연 제목'),
        ),
        migrations.AlterField(
            model_name='playcasting',
            name='casting',
            field=models.ImageField(upload_to='', verbose_name='배역 이미지'),
        ),
        migrations.AlterField(
            model_name='playimage',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='공연 관련 사진'),
        ),
        migrations.AlterField(
            model_name='playvideo',
            name='video_url',
            field=models.CharField(max_length=200, verbose_name='공연 관련 링크(극 공개, 티저, 인터뷰순)'),
        ),
    ]