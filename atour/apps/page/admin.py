from django.contrib import admin
from apps.page.models import Page, Callback

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
        (None, {
            'fields': (
                'title', 'slug', 'body', 'is_published',
            )
        }),
    )
    
    prepopulated_fields = {'slug': ('title',)} #Автоматическое заполнение поля слаг


class CallbackAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'fio', 'phone', 'message',
        'datetime_create', 'datetime_update', 'is_complete',
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
    
    list_filter = (
        'is_complete',
    )
    
    fieldsets = (
        (None, {
            'fields': (
                'fio', 'phone', 'message', 'is_complete',
            )
        }),
    )    


#Регистрация моделей в админ-панеле
admin.site.register(Page, PageAdmin)
admin.site.register(Callback, CallbackAdmin)

