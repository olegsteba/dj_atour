#from distutils.command.build import build
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator, MaxLengthValidator
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


PHONE_REGEX = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Допускаются только цифры'
)


class Callback(models.Model):
    """Обратный звонок"""
    fio = models.CharField(
       max_length=255,
       verbose_name='Ваше Ф.И.О.',
    )
    
    phone = models.CharField(
        max_length=17,
        validators=[PHONE_REGEX, MaxLengthValidator],
        verbose_name='Ваш номер телефона'
    )  
    
    message = models.TextField(
        verbose_name='Комментарий к заявке',
    )
    
    datetime_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    
    datetime_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )
    
    is_complete = models.BooleanField(
        default=False,
        verbose_name='Обработано',
    )    
    
    def __str__(self):
        return f"{self.fio} - {self.phone}"
    
    class Meta:
        verbose_name='Обратный звонок'
        verbose_name_plural='Обратные звоноки'
        ordering = ['-pk']
    
