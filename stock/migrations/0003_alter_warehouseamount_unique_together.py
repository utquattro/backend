# Generated by Django 4.2.5 on 2023-09-24 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_alter_productconfig_unique_together'),
        ('stock', '0002_alter_warehouseamount_product_item'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='warehouseamount',
            unique_together={('stock', 'product_item')},
        ),
    ]
