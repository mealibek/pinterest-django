# Generated by Django 4.2.7 on 2023-11-26 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_url_profileimage_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_image', to='profiles.profileimage'),
        ),
    ]
