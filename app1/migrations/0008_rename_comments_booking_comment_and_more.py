# Generated by Django 4.1.7 on 2023-03-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_menu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='comments',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='guest_count',
            new_name='guest_number',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='reservation_time',
        ),
        migrations.AlterField(
            model_name='booking',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]
