# Generated by Django 4.1.4 on 2022-12-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0007_machine_last_heartbeat"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.CharField(max_length=255, null=True),
        ),
    ]