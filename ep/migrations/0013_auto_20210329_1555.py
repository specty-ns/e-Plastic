# Generated by Django 3.0 on 2021-03-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0012_auto_20210329_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_placed',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_qty',
            field=models.BigIntegerField(),
        ),
    ]