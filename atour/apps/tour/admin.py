from django.contrib import admin
from apps.tour.models import Tour


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'slug', 'image', 'price', 
        'datetime_create', 'datetime_update', 
        'is_published',
        
    )
    
    list_display_links = (
        'id', 'title',
    )
    
    search_fields = (
        'title',
    )
    
    list_editable = (
        'is_published',
    )
    
    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'image', 'price', 
                'star', 'body', 'is_published',
            )
        }),
    )

    prepopulated_fields = {'slug': ('title',)} #Автоматическое заполнение поля слаг
    
    
#Регистрация моделей в админ-панеле
admin.site.register(Tour, TourAdmin)    
    