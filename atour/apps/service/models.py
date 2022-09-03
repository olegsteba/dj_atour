from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',        
    )

    slug = models.SlugField(
        max_length=255,
        unique=True, 
        db_index=True,
        verbose_name='Slug страницы',
    )
    
    image = models.ImageField(
        upload_to='service/%Y/%m/%d', 
        null=True,
        blank=True,
        verbose_name='Изображение',
    )        
    
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=0,
        verbose_name='Стоимость', 
    )
    
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='category_services',
        verbose_name='ID категории',
    )
    
    body = RichTextUploadingField(
        blank=True, 
        null=True,
        verbose_name='Описание', 
    )
    
    datetime_create = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания',
    )
    
    datetime_update = models.DateTimeField(
        auto_now=True, 
        verbose_name='Дата обновления',
    )
        
    is_published = models.BooleanField(
        default=True, 
        verbose_name='Опубликовано',
    )
        
    def __str__(self):
        return f"{self.title}"    

    def get_absolute_url(self):
        return reverse('service', kwargs={"service_slug": self.slug})
    
    class Meta:
        verbose_name='Услуга'
        verbose_name_plural='Услуги'
        

class Category(models.Model):
    name = models.CharField(
        max_length=255, 
        db_index=True, 
        verbose_name='Название',
    )    
    
    slug = models.SlugField(
        max_length=255, 
        unique=True, 
        db_index=True, 
        verbose_name='Slug категории',
    )
    
    image = models.ImageField(
        upload_to='category/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    
    in_two_rows = models.BooleanField(
        default=False, 
        verbose_name='В две строки',
    )
          
    body = RichTextUploadingField(
        null=True,
        blank=True,
        verbose_name='Описание',
    )
    
    datetime_create = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания',
    )
    
    datetime_update = models.DateTimeField(
        auto_now=True, 
        verbose_name='Дата обновления',
    )

    position = models.IntegerField(
        verbose_name='Позиция', 
        default=500,
    )
            
    is_published = models.BooleanField(
        default=True, 
        verbose_name='Опубликовано'
    )
        
    def __str__(self):
        return f"{self.name}"    

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_slug": self.slug})  

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering = ['position']
