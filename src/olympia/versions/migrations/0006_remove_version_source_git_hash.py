# Generated by Django 2.2.12 on 2020-05-22 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('versions', '0005_auto_20200518_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='source_git_hash',
        ),
    ]
