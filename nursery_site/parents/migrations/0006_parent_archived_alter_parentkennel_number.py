# Generated by Django 4.1.2 on 2023-02-28 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parents", "0005_parentkennel"),
    ]

    operations = [
        migrations.AddField(
            model_name="parent",
            name="archived",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="parentkennel",
            name="number",
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
    ]
