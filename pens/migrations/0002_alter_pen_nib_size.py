# Generated by Django 4.1 on 2022-08-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pens", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pen",
            name="nib_size",
            field=models.CharField(max_length=10),
        ),
    ]
