# Generated by Django 5.0.4 on 2024-05-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0013_alter_women_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Slug'),
        ),
    ]
