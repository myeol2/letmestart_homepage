# Generated by Django 2.1 on 2018-09-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20180909_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playmember',
            name='name',
            field=models.CharField(max_length=6, verbose_name='이름'),
        ),
    ]