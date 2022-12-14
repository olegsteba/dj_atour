# Generated by Django 4.1 on 2022-09-03 11:46

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug категории')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/%Y/%m/%d', verbose_name='Изображение')),
                ('in_two_rows', models.BooleanField(default=False, verbose_name='В две строки')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('datetime_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('datetime_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категогии',
            },
        ),
        migrations.RemoveField(
            model_name='service',
            name='in_two_rows',
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='category_services', to='service.category', verbose_name='ID категории'),
            preserve_default=False,
        ),
    ]
