# Generated by Django 5.0 on 2024-02-03 22:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userwallet",
            name="balance",
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
