from django.contrib import admin
from .models import Personnel, PersonnelWaiting


@admin.register(Personnel)
class PersonnelAdminModel(admin.ModelAdmin):
    list_display = "personnel_code", "first_name", "last_name"
    # readonly_fields = "personnel_code",
    search_fields = "personnel_code", "first_name", "last_name"


@admin.register(PersonnelWaiting)
class PersonnelWaitingModelAdmin(admin.ModelAdmin):
    list_display = "personnel_code", "barber_code", "reserved_date"
    search_fields = "personnel_code__personnel_code", "barber_code__barber_code", "reserved_date"
