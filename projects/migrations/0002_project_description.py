# Generated by Django 4.1.1 on 2022-09-12 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
