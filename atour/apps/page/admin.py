from django.contrib import admin
from apps.page.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'slug',
        'datetime_create', 'datetime_update', 'is_published',
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
    
    list_filter = (
        'is_published',
    )
    
    fieldsets = (
        (
            (None, {
                'fields': (
                    'title', 'slug', 'body', 'is_published',
                )
            }),
        )
    )
    
    prepopulated_fields = {'slug': ('title',)} #Автоматическое заполнение поля слаг

#Регистрация моделей в админ-панеле
admin.site.register(Page, PageAdmin)

