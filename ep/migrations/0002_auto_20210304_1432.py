# Generated by Django 2.0 on 2021-03-04 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlasticRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField()),
                ('request_quantity', models.BigIntegerField(default=0)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('comp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Company')),
                ('plasticc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.PlasticC')),
                ('pproduct_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.PlasticProduct')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.BigIntegerField()),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='ep.Master')),
            ],
        ),
        migrations.RemoveField(
            model_name='requestbutton',
            name='comp_id',
        ),
        migrations.RemoveField(
            model_name='requestbutton',
            name='plasticc_id',
        ),
        migrations.RemoveField(
            model_name='requestbutton',
            name='pproduct_id',
        ),
        migrations.AddField(
            model_name='checkout',
            name='payment_status',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.DeleteModel(
            name='RequestButton',
        ),
    ]
