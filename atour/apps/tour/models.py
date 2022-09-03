from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Tour(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='Slug тура',
    )
    
    image = models.ImageField(
        upload_to='tour/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=0,
        verbose_name='Стоимость', 
    )
    
    star = models.PositiveSmallIntegerField(
        choices=[
            (1, 'Одна звезда'),
            (2, 'Две звезды'),
            (3, 'Три звезды'),
            (4, 'Четыре звезды'),
            (5, 'Пять звезд'),
        ],
        verbose_name='Количество звезд',
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
        
    is_published = models.BooleanField(
        default=True, 
        verbose_name='Опубликовано',
    )
        
    def __str__(self):
        return f"{self.title}"    

    def get_absolute_url(self):
        return reverse('tour', kwargs={"tour_slug": self.slug})
    
    class Meta:
        verbose_name='Тур'
        verbose_name_plural='Туры'
        