# Generated by Django 3.0 on 2021-03-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0006_auto_20210312_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='comp_postalcode',
            field=models.BigIntegerField(null=True),
        ),
    ]