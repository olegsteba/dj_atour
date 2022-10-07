from django.db import models
from django.urls import reverse


class Feedback(models.Model):
    """Отзыв"""
    fio = models.CharField(
        max_length=255,
        verbose_name='Ваше Ф.И.О',
    )
    
    rating = models.PositiveSmallIntegerField(
        choices=[
            (None, 'Выберите рейтинг'),
            (1, 'Одна звезда'),
            (2, 'Две звезды'),
            (3, 'Три звезды'),
            (4, 'Четыре звезды'),
            (5, 'Пять звезд'),
        ],
        verbose_name='Рейтинг',
    )
    
    body = models.TextField(
        verbose_name='Отзыв',
    )
    
    datetime_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    
    datetile_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )
    
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовано',
    )
    
    def __str__(self):
        return f"{self.datetime_create} - {self.fio}"
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-pk']
    
    

    
