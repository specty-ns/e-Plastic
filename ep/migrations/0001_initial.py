# Generated by Django 2.0 on 2021-02-16 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_price', models.BigIntegerField(default=0)),
                ('cart_quantity', models.BigIntegerField(default=1)),
                ('cart_date', models.DateTimeField()),
                ('cart_subtotal', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_total', models.BigIntegerField(default=0)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.AddToCart')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=50)),
                ('comp_address', models.CharField(max_length=500)),
                ('comp_contact', models.BigIntegerField()),
                ('comp_image', models.ImageField(upload_to='companyimg/')),
                ('comp_fb', models.CharField(max_length=1000)),
                ('comp_insta', models.CharField(max_length=1000)),
                ('comp_linkedin', models.CharField(max_length=1000)),
                ('comp_twitter', models.CharField(max_length=1000)),
                ('comp_website', models.CharField(max_length=200)),
                ('owner_fname', models.CharField(max_length=50)),
                ('owner_lname', models.CharField(max_length=50)),
                ('owner_gender', models.CharField(max_length=50)),
                ('owner_contact', models.CharField(max_length=50)),
                ('owner_email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('contact', models.BigIntegerField()),
                ('address', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('postalcode', models.BigIntegerField(default=0)),
                ('image', models.ImageField(upload_to='customerimg/')),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('otp', models.BigIntegerField(default=123)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlasticC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_name', models.CharField(max_length=50)),
                ('pc_address', models.CharField(max_length=50)),
                ('pc_contact', models.BigIntegerField()),
                ('pc_image', models.ImageField(upload_to='plasticcimg/')),
                ('pc_fb', models.CharField(max_length=1000)),
                ('pc_insta', models.CharField(max_length=1000)),
                ('pc_linkedin', models.CharField(max_length=1000)),
                ('pc_twitter', models.CharField(max_length=1000)),
                ('pc_website', models.CharField(max_length=200)),
                ('owner_fname', models.CharField(max_length=50)),
                ('owner_lname', models.CharField(max_length=50)),
                ('owner_gender', models.CharField(max_length=50)),
                ('owner_contact', models.BigIntegerField(default=0)),
                ('owner_email', models.EmailField(max_length=50)),
                ('master_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Master')),
            ],
        ),
        migrations.CreateModel(
            name='PlasticProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pproduct_name', models.CharField(max_length=100)),
                ('pproduct_date', models.DateTimeField()),
                ('pproduct_price', models.BigIntegerField(default=0)),
                ('pproduct_image', models.ImageField(upload_to='pproductimg/')),
                ('pproduct_quantity', models.BigIntegerField(default=0)),
                ('plasticc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.PlasticC')),
            ],
        ),
        migrations.CreateModel(
            name='RecycleProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rproduct_name', models.CharField(max_length=100)),
                ('rproduct_date', models.DateTimeField()),
                ('rproduct_price', models.BigIntegerField(default=0)),
                ('rproduct_image', models.ImageField(upload_to='rproductimg/')),
                ('rproduct_quantity', models.BigIntegerField(default=0)),
                ('rproduct_desc', models.CharField(max_length=500)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Company')),
            ],
        ),
        migrations.CreateModel(
            name='RequestButton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField()),
                ('request_quantity', models.BigIntegerField(default=0)),
                ('comp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Company')),
                ('plasticc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.PlasticC')),
                ('pproduct_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.PlasticProduct')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='master_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Master'),
        ),
        migrations.AddField(
            model_name='company',
            name='master_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Master'),
        ),
        migrations.AddField(
            model_name='addtocart',
            name='cust_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.Customer'),
        ),
        migrations.AddField(
            model_name='addtocart',
            name='rp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep.RecycleProduct'),
        ),
    ]
