from django.contrib import admin
from apps.service.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'slug', 'price',
        'datetime_create', 'datetime_update', 
        'in_two_rows', 'is_published',
    )
    
    list_display_links = (
        'id', 'title',
    )
    
    search_fields = (
        'title',
    )
    
    list_editable = (
        'in_two_rows', 'is_published',
    )
    
    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'image', 'price',
                'body', 'in_two_rows', 'is_published',
            )
        }),
    )

    prepopulated_fields = {'slug': ('title',)} #Автоматическое заполнение поля слаг

#Регистрация моделей в админ-панеле
admin.site.register(Service, ServiceAdmin)
