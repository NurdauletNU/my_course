from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.ClothCategory)
admin.site.register(models.Cloth)
admin.site.register(models.ClothSet)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    # list_editable = ('is_completed',)
    list_filter = ('title',)
    fieldsets = (
        ('Основное', {'fields': (
            'title',
        )}),
    )
    search_fields = [
        'title'
    ]


admin.site.register(models.Position, PositionAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'tabel_num', 'position')
    list_display_links = ('last_name', 'tabel_num')
    list_editable = ('first_name',)
    list_filter = ('first_name', 'last_name', 'patronymic', 'tabel_num', 'position')
    fieldsets = (
        ('Основное', {'fields': (
            'first_name', 'last_name', 'patronymic', 'position'
        )},),
        ('Вспомагательное', {'fields': ('tabel_num',)
                             },),
    )
    search_fields = [
        'first_name', 'last_name', 'patronymic', 'tabel_num', 'position'
    ]


admin.site.register(models.Person, PersonAdmin)
