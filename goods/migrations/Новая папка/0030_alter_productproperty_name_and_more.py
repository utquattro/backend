# Generated by Django 4.2.5 on 2023-09-22 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0029_alter_productproperty_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productproperty',
            name='name',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='value',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
