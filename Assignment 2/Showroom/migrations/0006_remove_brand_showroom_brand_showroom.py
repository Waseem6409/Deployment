# Generated by Django 4.2.4 on 2023-08-12 03:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Showroom", "0005_brand_created_at_engine_created_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="brand",
            name="showroom",
        ),
        migrations.AddField(
            model_name="brand",
            name="showroom",
            field=models.ManyToManyField(default="", to="Showroom.showroom"),
        ),
    ]
