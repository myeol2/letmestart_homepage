# Generated by Django 2.1 on 2018-09-10 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20180909_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playmember',
            options={'ordering': ['-position', 'admission_order_letme', 'name'], 'verbose_name': '함께한 사람들'},
        ),
    ]
