# Generated by Django 4.1 on 2023-05-14 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("homerental", "0004_rename_home_homeadd"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homeadd",
            name="home_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="homerental.homeowner"
            ),
        ),
    ]
