# Generated by Django 3.0 on 2021-02-27 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ep', '0002_acceptrequest_transaction'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RequestButton',
            new_name='PlasticRequest',
        ),
    ]