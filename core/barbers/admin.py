from django.contrib import admin
from .models import Barber, BarberHairCut


@admin.register(Barber)
class BarberModelAdmin(admin.ModelAdmin):
    list_display = "barber_code", "first_name", "last_name"
    # readonly_fields = "barber_code",
    search_fields = "barber_code", "first_name", "last_name", "limit"


@admin.register(BarberHairCut)
class BarberHairCutModelAdmin(admin.ModelAdmin):
    list_display = "barber_code", "personnel_code", "date"
    # readonly_fields = "barber_code", "personnel_code", "date"
    search_fields = "barber_code__barber_code", "personnel_code__personnel_code", "date"
