# Generated by Django 3.0 on 2021-03-18 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_collection', models.FloatField()),
                ('wastage', models.FloatField()),
                ('usage', models.FloatField()),
                ('collection_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_total', models.BigIntegerField(default=0)),
                ('payment_status', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PlasticRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField()),
                ('request_quantity', models.BigIntegerField(default=0)),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('cust_number', models.BigIntegerField()),
                ('sc_date_time', models.DateTimeField()),
                ('sc_comment', models.CharField(max_length=200)),
                ('pickup_status', models.CharField(default='pending', max_length=50)),
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
            model_name='company',
            name='comp_city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='company',
            name='comp_postalcode',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='comp_state',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postalcode',
            field=models.BigIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
        migrations.DeleteModel(
            name='RequestButton',
        ),
        migrations.AddField(
            model_name='scheduleorder',
            name='cust_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Customer'),
        ),
        migrations.AddField(
            model_name='plasticrequest',
            name='comp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Company'),
        ),
        migrations.AddField(
            model_name='plasticrequest',
            name='plasticc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.PlasticC'),
        ),
        migrations.AddField(
            model_name='plasticrequest',
            name='pproduct_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.PlasticProduct'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Customer'),
        ),
        migrations.AddField(
            model_name='customerdata',
            name='cust_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Customer'),
        ),
        migrations.AddField(
            model_name='customerdata',
            name='plastic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.PlasticC'),
        ),
    ]
