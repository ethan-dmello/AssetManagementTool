from django.db import models
from datetime import date


class Equipment(models.Model):
    asset_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    procured_date = models.DateField(blank=True, null=True)
    warranty_expiration_date = models.DateField(blank=True, null=True)
    assigned_to = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=15,
        choices=[
            ("Active", "Active"),
            ("Inactive", "Inactive"),
            ("Under Repair", "Under Repair"),
        ],
        default="Active",
    )
    usage_type = models.CharField(
        max_length=20,
        choices=[
            ("Laptop", "Laptop"),
            ("Desktop", "Desktop"),
            ("Phone", "Phone"),
            ("iPad", "iPad"),
        ],
        blank=True,
        null=True,
    )
    added_by = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.asset_id} - {self.name}"


class OwnershipLog(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipment.name} assigned to {self.assigned_to}"
