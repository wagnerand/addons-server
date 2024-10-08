# Generated by Django 4.2.15 on 2024-08-29 11:54

from django.db import migrations

def create_cinder_appeals(apps, schema_editor):
    AbuseReport = apps.get_model('abuse', 'AbuseReport')
    CinderAppeal = apps.get_model('abuse', 'CinderAppeal')
    abuse_qs = AbuseReport.objects.filter(
        # i.e. we have an appeal job linked,
        appellant_job__isnull=False,
        # and there is an fk to the decision that was appealed,
        cinder_job__decision__isnull=False,
        # but there is no CinderAppeal instance already.
        cinderappeal__isnull=True,
    )
    CinderAppeal.objects.bulk_create(
        [
            CinderAppeal(decision=report.cinder_job.decision, reporter_report=report)
            for report in abuse_qs
        ]
    )

class Migration(migrations.Migration):

    dependencies = [
        ('abuse', '0038_cinderjob_forwarded_to_job_and_more'),
    ]

    operations = [
        migrations.RunPython(create_cinder_appeals, reverse_code=migrations.RunPython.noop)
    ]
