import django_tables2 as tables
from .models import Equipment

class EquipmentTable(tables.Table):
    class Meta:
        model = Equipment
        template_name = "django_tables2/bootstrap4.html"
        fields = ("asset_id", "name", "description", "procured_date", "assigned_to", "status")
