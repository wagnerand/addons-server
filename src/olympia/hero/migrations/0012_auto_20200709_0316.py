# Generated by Django 2.2.14 on 2020-07-09 03:16

from django.db import migrations, models
import olympia.hero.models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0011_auto_20200624_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryheroimage',
            name='custom_image',
            field=models.ImageField(upload_to=olympia.hero.models.hero_image_directory, verbose_name='custom image path'),
        ),
    ]
