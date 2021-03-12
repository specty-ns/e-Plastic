# Generated by Django 2.0 on 2021-03-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0005_auto_20210304_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='comp_city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='company',
            name='comp_postalcode',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='comp_state',
            field=models.CharField(default='', max_length=50),
        ),
    ]