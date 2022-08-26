from django.contrib import admin
from apps.menu.models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    ordering = ('position',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',]
    inlines = [MenuItemInline,]


admin.site.register(Menu, MenuAdmin)
