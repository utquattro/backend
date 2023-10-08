# Generated by Django 4.2.5 on 2023-10-04 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0015_alter_propertyname_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="categorypropertyconfig",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="categorypropertyconfig",
            name="property_name",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="goods.propertyname",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="categorypropertyconfig",
            unique_together={("property_name", "category")},
        ),
        migrations.RemoveField(
            model_name="categorypropertyconfig",
            name="product_property",
        ),
    ]
