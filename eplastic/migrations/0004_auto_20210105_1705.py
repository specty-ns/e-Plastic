# Generated by Django 2.0 on 2021-01-05 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eplastic', '0003_master_otp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plasticc',
            old_name='pc_gender',
            new_name='pc_address',
        ),
        migrations.RemoveField(
            model_name='plasticc',
            name='pc_lname',
        ),
    ]