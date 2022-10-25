from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator, MaxLengthValidator
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
        return reverse('tour_detail', kwargs={"tour_slug": self.slug})
    
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


PHONE_REGEX = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Допускаются только цифры'
)

class Order(models.Model):
    """Заказ тура""" 
    fio = models.CharField(
        max_length=255,
        verbose_name='Ваше Ф.И.О.',
    )

    phone = models.CharField(
        max_length=17,
        validators=[PHONE_REGEX, MaxLengthValidator],
        verbose_name='Ваш номер телефона'
    )  

    email = models.EmailField(
        max_length=254, 
        verbose_name='Электронный адрес',
    )        

    tour = models.ForeignKey(
        'Tour',
        on_delete=models.PROTECT,
        related_name="tour_order",
        verbose_name="Тур",        
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
        return f"{self.fio} - {self.tour}"
    
    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'
        ordering = ['-pk']
        