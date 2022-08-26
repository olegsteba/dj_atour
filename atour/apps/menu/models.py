from django.db import models


class Menu(models.Model):
    """Основная модель меню"""
    name = models.CharField(
        verbose_name='Наименование',
        max_length=256,
    )
    
    slug = models.SlugField(
        verbose_name='Код',
        max_length=256,
        unique=True,
        db_index=True,
    )
    
    class Meta:
        verbose_name='Меню'
        verbose_name_plural='Меню'
        
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        """
        Переупорядочивание элементов от 10 и выше с интервалом 10.
        Для удобного добавления новых элементов в середину.
        """
        
        super(Menu, self).save(*args, **kwargs)
        
        current = 10
        for item in MenuItem.objects.filter(menu=self).order_by('position'):
            item.position = current
            item.save()
            current += 10
            

class MenuItem(models.Model):
    LINK_TARGET_CHOICES = (
        ('_blank', '_blank'),
        ('_top', '_top'),
        ('_parent', '_parent'),
    )
    
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu_menu_item',
        verbose_name='ID меню',
    )
    
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256,
    )
    
    url = models.CharField(
        verbose_name='URL адрес',
        max_length=256,
        help_text='URL или URI для страницы, например /about/ или http://a-tour.ru/',
    )
    
    target = models.CharField(
        verbose_name='Метод',
        max_length=10,
        choices=LINK_TARGET_CHOICES,
        null=True,
        blank=True,
    )    

    position = models.IntegerField(
        verbose_name='Позиция', 
        default=500,
    )

    authorized_only = models.BooleanField(
        verbose_name='Для авторизированных',
        blank=True,
        default=False,
        help_text='Если установить, то пункт меню будет показан только для авторизированных пользователей'
        )

    anonymous_only = models.BooleanField(
        verbose_name='Для анонимных',
        blank=True,
        default=False,
        help_text='Если установить, то пункт меню будет показан только для не авторизированных пользователей'
        )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return f'{self.menu.slug} {self.position}. {self.title}'
