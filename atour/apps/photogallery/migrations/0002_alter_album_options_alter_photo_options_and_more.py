# Generated by Django 4.1 on 2022-09-07 07:21

import apps.photogallery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-pk'], 'verbose_name': 'Альбом', 'verbose_name_plural': 'Альбомы'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=None, upload_to=apps.photogallery.models.upload_album_image, verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
