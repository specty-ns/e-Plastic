# Generated by Django 2.0 on 2021-01-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasticc',
            name='owner_contact',
            field=models.BigIntegerField(blank=2),
        ),
    ]
