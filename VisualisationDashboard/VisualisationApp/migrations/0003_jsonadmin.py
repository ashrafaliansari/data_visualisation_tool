# Generated by Django 4.2.4 on 2023-09-02 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("VisualisationApp", "0002_rename_data_jsondata"),
    ]

    operations = [
        migrations.CreateModel(
            name="JsonAdmin",
            fields=[
                (
                    "jsondata_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="VisualisationApp.jsondata",
                    ),
                ),
            ],
            bases=("VisualisationApp.jsondata",),
        ),
    ]