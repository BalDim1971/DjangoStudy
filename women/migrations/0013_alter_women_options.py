# Generated by Django 5.0.4 on 2024-05-22 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0012_alter_women_cat_alter_women_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create'], 'verbose_name': 'Известная женщина', 'verbose_name_plural': 'Известные женщины'},
        ),
    ]
