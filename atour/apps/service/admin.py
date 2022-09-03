from django.contrib import admin
from apps.service.models import Service, Category


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'slug', 'category', 'price',
        'datetime_create', 'datetime_update', 'is_published',
    )
    
    list_display_links = (
        'id', 'title',
    )
    
    search_fields = (
        'title', 'category',
    )
    
    list_editable = (
        'is_published',
    )
    
    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'category', 'image',
                'price', 'body', 'is_published',
            )
        }),
    )

    prepopulated_fields = {'slug': ('title',)} #Автоматическое заполнение поля слаг


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'slug', 'image',
        'datetime_create', 'datetime_update',
        'in_two_rows', 'position', 'is_published',
    )
    
    list_display_links = (
        'id', 'name',
    )
    
    search_fields = (
        'name',
    )
    
    list_editable = (
        'in_two_rows', 'position', 'is_published',
    )
    
    list_filter = (
        'name',
    )
    
    fieldsets = (
        (None, {
            'fields': (
                'name', 'slug', 'image', 'in_two_rows', 
                'body', 'position', 'is_published',
            )
        }),
    )    
    
    prepopulated_fields = {'slug': ('name',)} #Автоматическое заполнение slug
    

#Регистрация моделей в админ-панеле
admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
