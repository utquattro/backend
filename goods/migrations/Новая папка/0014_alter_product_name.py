# Generated by Django 4.2.5 on 2023-09-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0013_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(blank=True, default='1', max_length=250),
        ),
    ]
