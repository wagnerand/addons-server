# Generated by Django 2.2.13 on 2020-06-12 16:04

from django.db import migrations, models

def backfill_old_banned_users(apps, schema_editor):
    # We already attempted this:
    # https://github.com/mozilla/addons-server/blob/2019.08.15/src/olympia/migrations/1116-add-banned-field.sql  # NOQA
    # but it only backfilled accounts that had both fxa_id AND email set, so
    # ignored older accounts that didn't have an fxa_id, for example.
    UserProfile = apps.get_model('users', 'UserProfile')
    qs = UserProfile.objects.filter(
        deleted=True, banned=None).exclude(email=None, fxa_id=None)
    qs.update(banned=models.F('modified'))

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(backfill_old_banned_users)
    ]
