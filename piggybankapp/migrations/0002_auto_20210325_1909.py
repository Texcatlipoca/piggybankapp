# Generated by Django 3.1.7 on 2021-03-25 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piggybankapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='status',
            new_name='test',
        ),
    ]
