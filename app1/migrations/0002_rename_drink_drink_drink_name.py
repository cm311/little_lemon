# Generated by Django 4.1.7 on 2023-03-18 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drink',
            old_name='drink',
            new_name='drink_name',
        ),
    ]
