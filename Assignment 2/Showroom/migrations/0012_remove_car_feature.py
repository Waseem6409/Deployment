# Generated by Django 4.2.4 on 2023-08-14 06:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Showroom", "0011_car_engine_car_feature_alter_brand_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="feature",
        ),
    ]
