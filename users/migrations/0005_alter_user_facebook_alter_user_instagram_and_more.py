# Generated by Django 5.0.7 on 2024-07-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_twitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook',
            field=models.CharField(blank=True, default='https://www.facebook.com/', max_length=50, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.CharField(blank=True, default='https://telegram.org/', max_length=50, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, default='https://www.instagram.com/', max_length=50, null=True, verbose_name='Telegram'),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, default='https://x.com/', max_length=50, null=True, verbose_name='Twitter'),
        ),
    ]
