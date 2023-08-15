# Generated by Django 4.2.4 on 2023-08-12 00:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("Showroom", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="car",
            name="model",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="Showroom.model",
            ),
        ),
        migrations.AddField(
            model_name="model",
            name="brand",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="Showroom.brand",
            ),
        ),
        migrations.AlterField(
            model_name="model",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]
