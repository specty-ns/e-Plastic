# Generated by Django 2.0 on 2021-02-22 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0003_auto_20210222_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='made_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='ep.Master'),
        ),
    ]