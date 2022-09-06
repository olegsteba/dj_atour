from django.db import models
from django.urls import reverse
from datetime import datetime

def upload_album_image(instance, filename):
    prefix = int(datetime.now().timestamp())
    return f"album/{instance.album.slug}/{prefix}_{filename}"

class Album(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название',        
    )

    slug = models.SlugField(
        max_length=255,
        unique=True, 
        db_index=True,
        verbose_name='Slug альбома',
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
        return reverse('album_detail', kwargs={"album_slug": self.slug})
    
    class Meta:
        verbose_name='Альбом'
        verbose_name_plural='Альбомы'
        ordering = ['-pk']


class Photo(models.Model):
    album = models.ForeignKey(
        'Album', 
        on_delete=models.CASCADE,
        related_name='album_photos',
        verbose_name='ID альбома',
    )
    
    image = models.ImageField(
        upload_to=upload_album_image,
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    
    def __str__(self):
        return f"{self.album.title}"
        
    class Meta:
        verbose_name='Фотография'
        verbose_name_plural='Фотографии'    
