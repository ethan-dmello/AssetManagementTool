from django import forms
from .models import Equipment


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = [
            'asset_id',
            'name',
            'description',
            'procured_date',
            'warranty_expiration_date',
            'assigned_to',
            'location',
            'status',
            'usage_type',
        ]
        widgets = {
            'asset_id': forms.TextInput(attrs={'placeholder': 'Enter Asset ID', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter Equipment Name', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter Description', 'class': 'form-control'}),
            'procured_date': forms.DateInput(
                format='%d/%m/%Y',
                attrs={'placeholder': 'DD/MM/YYYY', 'class': 'form-control', 'type': 'text'}
            ),
            'warranty_expiration_date': forms.DateInput(
                format='%d/%m/%Y',
                attrs={'placeholder': 'DD/MM/YYYY', 'class': 'form-control', 'type': 'text'}
            ),
            'assigned_to': forms.TextInput(attrs={'placeholder': 'Enter Name or Department', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter Location', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'usage_type': forms.Select(attrs={'class': 'form-select'}),
        }
