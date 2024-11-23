from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Equipment, OwnershipLog
from .forms import EquipmentForm
from django.shortcuts import get_object_or_404, redirect
from .models import Equipment


@login_required
def equipment_list(request):
    query = request.GET.get('search', '')
    equipment = Equipment.objects.filter(name__icontains=query)
    paginator = Paginator(equipment, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'inventory/equipment_list.html', {
        'equipment': page_obj,
        'search_query': query,
    })


@login_required
def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    ownership_logs = OwnershipLog.objects.filter(equipment=equipment).order_by('-start_date')
    return render(request, 'inventory/equipment_detail.html', {
        'equipment': equipment,
        'ownership_logs': ownership_logs,
    })


@login_required
def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.procured_date = form.cleaned_data['procured_date']
            equipment.warranty_expiration_date = form.cleaned_data['warranty_expiration_date']
            equipment.save()

            OwnershipLog.objects.create(
                equipment=equipment,
                assigned_to=equipment.assigned_to or "Unassigned",
                start_date=date.today(),
            )

            return redirect('equipment_list')
    else:
        form = EquipmentForm()

    return render(request, 'inventory/add_equipment.html', {'form': form})


@login_required
def edit_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            new_assigned_to = form.cleaned_data['assigned_to']
            if equipment.assigned_to != new_assigned_to:
                OwnershipLog.objects.filter(equipment=equipment, end_date__isnull=True).update(end_date=date.today())
                OwnershipLog.objects.create(
                    equipment=equipment,
                    assigned_to=new_assigned_to or "Unassigned",
                    start_date=date.today(),
                )
            form.save()
            return redirect('equipment_detail', pk=pk)
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'inventory/edit_equipment.html', {'form': form, 'equipment': equipment})

@login_required
def delete_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')
    return redirect('equipment_list')  # Fallback for non-POST requests

