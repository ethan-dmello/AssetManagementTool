from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("equipment/", views.equipment_list, name="equipment_list"),
    path("equipment/add/", views.add_equipment, name="add_equipment"),
    path("equipment/<int:pk>/", views.equipment_detail, name="equipment_detail"),
    path("equipment/<int:pk>/edit/", views.edit_equipment, name="edit_equipment"),
    path("equipment/<int:pk>/delete/", views.delete_equipment, name="delete_equipment"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
