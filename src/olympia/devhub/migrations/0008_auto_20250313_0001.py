# Generated by Django 4.2.19 on 2025-03-13 00:01

from django.db import migrations

from olympia.core.db.migrations import CreateWaffleSwitch

class Migration(migrations.Migration):

    dependencies = [
        ('devhub', '0007_surveyresponse_surveyresponse_unique_survey_user'),
    ]

    operations = [
        CreateWaffleSwitch('enable_dev_experience_survey')
    ]
