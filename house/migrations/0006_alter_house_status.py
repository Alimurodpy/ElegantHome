# Generated by Django 5.0.7 on 2024-07-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_alter_gallery_house_alter_house_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(choices=[('new_to_old', 'new_to_old'), ('for_rent', 'for_rent'), ('for_sale', 'for_sale')], max_length=20, verbose_name='status'),
        ),
    ]
