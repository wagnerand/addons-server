# Generated by Django 2.2.16 on 2020-11-04 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("promoted", "0014_promotedsubscription_onboarding_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="promotedsubscription",
            name="stripe_subscription_id",
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
