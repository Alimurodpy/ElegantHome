# Generated by Django 5.0.6 on 2025-03-17 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0013_district_house_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='house',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='houses_district', to='house.district', verbose_name='district'),
        ),
    ]
