# Generated by Django 4.2.5 on 2023-09-21 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0022_productitem_variation_productitem_variation_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='variation',
        ),
        migrations.RemoveField(
            model_name='productitem',
            name='variation_option',
        ),
    ]
