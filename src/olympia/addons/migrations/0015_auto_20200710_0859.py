# Generated by Django 2.2.14 on 2020-07-10 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.manager
import olympia.amo.models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0014_remove_addon_view_source'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addonuser',
            options={'base_manager_name': 'unfiltered'},
        ),
        migrations.AlterModelManagers(
            name='addonuser',
            managers=[
                ('unfiltered', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='addon',
            name='authors',
            field=olympia.amo.models.FilterableManyToManyField(related_name='addons', through='addons.AddonUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='addonuser',
            name='role',
            field=models.SmallIntegerField(choices=[(5, 'Owner'), (4, 'Developer'), (6, '(Deleted)')], default=5),
        ),
    ]
