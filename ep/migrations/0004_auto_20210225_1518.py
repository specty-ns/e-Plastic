# Generated by Django 2.0 on 2021-02-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0003_auto_20210225_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
    ]
