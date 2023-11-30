# Generated by Django 4.2.7 on 2023-11-30 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0002_rename_website_pin_origin_pin_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Pin Description'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Pin Title'),
        ),
    ]
