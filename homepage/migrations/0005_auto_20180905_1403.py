# Generated by Django 2.1 on 2018-09-05 14:03

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20180905_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='poster',
            field=models.ImageField(upload_to=homepage.models.play_media_path, verbose_name='포스터 이미지'),
        ),
        migrations.AlterField(
            model_name='playcasting',
            name='casting',
            field=models.ImageField(upload_to=homepage.models.play_media_path, verbose_name='배역 이미지'),
        ),
        migrations.AlterField(
            model_name='playimage',
            name='image',
            field=models.ImageField(upload_to=homepage.models.play_media_path, verbose_name='공연 관련 사진'),
        ),
    ]