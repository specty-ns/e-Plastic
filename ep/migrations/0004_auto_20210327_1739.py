# Generated by Django 3.0 on 2021-03-27 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0003_order_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.AddToCart'),
        ),
    ]