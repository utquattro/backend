# Generated by Django 4.2.5 on 2023-09-24 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0053_remove_productsku_product_productitem_and_more'),
        ('stock', '0003_alter_warehouseamount_product_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseamount',
            name='product_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.productitem'),
        ),
    ]
