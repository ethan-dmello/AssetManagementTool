from django.contrib import admin
from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'asset_id',
        'name',
        'status',
        'location',
        'assigned_to',
        'warranty_expiration_date',
        'usage_type',
        'added_by',
        'last_updated',
    )
    list_filter = ('status', 'usage_type', 'location')
    search_fields = ('asset_id', 'name', 'description')
