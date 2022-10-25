from django.contrib import admin
from apps.tour.models import Tour, Order


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
    

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'fio', 'phone', 'email', 'tour', 
        'datetime_create', 'datetime_update', 
        'is_complete',
        
    )
    
    list_display_links = (
        'id', 'fio',
    )
    
    search_fields = (
        'fio',
    )
    
    list_editable = (
        'is_complete',
    )
    
    fieldsets = (
        (None, {
            'fields': (
                'fio', 'phone', 'email', 'tour', 
                'message', 'is_complete',
            )
        }),
    )
    
#Регистрация моделей в админ-панеле
admin.site.register(Tour, TourAdmin)    
admin.site.register(Order, OrderAdmin)   
    