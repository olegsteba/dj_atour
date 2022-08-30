from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Service(models.Model):
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
    
    image = models.ImageField(
        upload_to='service/%Y/%m/%d', 
        verbose_name='Изображение',
        null=True,
        blank=True,
    )        
    
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=0)
    
    body = RichTextUploadingField(verbose_name='Описание', blank=True, null=True)
    
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    datetime_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    in_two_rows = models.BooleanField(default=False, verbose_name='В две строки')
    
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name='Услуга'
        verbose_name_plural='Услуги'
        
    def __str__(self):
        return f"{self.title}"    

    def get_absolute_url(self):
        return reverse('service', kwargs={"service_slug": self.slug})


