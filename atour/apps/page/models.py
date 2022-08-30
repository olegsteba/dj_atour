from distutils.command.build import build
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255,
    )

    slug = models.SlugField(
        verbose_name='Slug страницы',
        max_length=255,
        unique=True, 
        db_index=True,
    )
        
    body = RichTextUploadingField(verbose_name='Описание', blank=True, null=True)
    
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    datetime_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name='Страница'
        verbose_name_plural='Страницы'
        
    def __str__(self):
        return f"{self.title}"    

    def get_absolute_url(self):
        return reverse('page', kwargs={"page_slug": self.slug})
