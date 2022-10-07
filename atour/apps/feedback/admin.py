from django.contrib import admin
from apps.feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'fio', 'datetime_create', 'is_published',
    )
    
    list_display_links = (
        'id', 'fio',
    )
    
    search_field = ('fio',)
    
    list_editable = (
        'is_published',
    )

    fieldsets = (
        (None, {
            'fields': (
                'fio', 'rating', 'body', 'is_published',
            )
        }),
    )
    

#Регистрация моделей в админ-панели
admin.site.register(Feedback, FeedbackAdmin)
