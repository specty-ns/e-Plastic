# Generated by Django 2.0 on 2021-02-11 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_price', models.BigIntegerField(default=0)),
                ('cart_quantity', models.BigIntegerField(default=0)),
                ('cart_date', models.DateTimeField()),
                ('cart_totle', models.BigIntegerField(default=0)),
                ('cart_subtotle', models.BigIntegerField(default=0)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Customer')),
                ('rp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.RecycleProduct')),
            ],
        ),
    ]
