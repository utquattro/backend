# Generated by Django 4.2.5 on 2023-09-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Copyright',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaySystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_system_name', models.TextField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Socical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('link', models.TextField(blank=True, max_length=500)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(blank=True, default=True)),
            ],
        ),
    ]
