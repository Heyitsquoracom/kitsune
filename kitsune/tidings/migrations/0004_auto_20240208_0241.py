# Generated by Django 4.2.9 on 2024-02-08 02:41

from django.db import migrations


def delete_watches(apps, schema_editor):
    Watch = apps.get_model("tidings", "Watch")
    Watch.objects.filter(user__is_active=False).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("tidings", "0003_alter_watchfilter_value"),
    ]

    operations = [
        migrations.RunPython(delete_watches, migrations.RunPython.noop)
    ]
