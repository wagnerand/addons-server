# Generated by Django 2.2.6 on 2019-10-09 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yara', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yararesult',
            name='has_matches',
            field=models.NullBooleanField(),
        ),
        migrations.AddIndex(
            model_name='yararesult',
            index=models.Index(fields=['has_matches'], name='yara_result_has_mat_eba666_idx'),
        ),
    ]
