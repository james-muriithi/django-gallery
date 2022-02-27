# Generated by Django 4.0.2 on 2022-02-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_category_options_category_slug_location_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, null=b'I01\n', unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='slug',
            field=models.SlugField(max_length=100, null=b'I01\n', unique=True),
        ),
    ]
