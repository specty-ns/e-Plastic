# Generated by Django 2.0 on 2021-02-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0002_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.BigIntegerField(),
        ),
    ]