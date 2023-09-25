# Generated by Django 4.2.5 on 2023-09-22 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0034_remove_propertyproduct_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyproduct',
            name='value',
        ),
        migrations.AddField(
            model_name='propertyproduct',
            name='property_value',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.valueproperty'),
        ),
    ]
