# Generated by Django 2.1 on 2018-09-10 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20180910_0233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playmember',
            options={'ordering': ['admission_order_letme', 'name'], 'verbose_name': '함께한 사람들'},
        ),
    ]