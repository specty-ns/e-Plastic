# Generated by Django 3.1 on 2021-04-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0002_addtocart_order_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recycleproduct',
            name='rproduct_quantity',
            field=models.PositiveIntegerField(),
        ),
    ]