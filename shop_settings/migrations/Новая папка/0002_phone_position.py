# Generated by Django 4.2.5 on 2023-09-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='position',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
