from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'firts_name', 'last_name', 'phone',
    ordering = 'id', # Ordena por id. "-id" Ordena de mode descrecente
    # list_filter = 'created_date'
    search_fields = 'id', 'firts_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'firts_name', 'last_name',
    list_display_links = 'id', 'phone',