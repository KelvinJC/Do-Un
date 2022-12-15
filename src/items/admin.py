from django.contrib import admin
from .models import Item

# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity', 'id', 'time_created', 'is_done', 'time_done', 'description', 'image_url', 'image')
    ordering = ('time_created',) # ('-name') for reverse order alphabetically
    search_fields = ('user', 'description')
    readonly_fields = ('id',)

