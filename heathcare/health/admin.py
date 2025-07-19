from django.contrib import admin
from .models import Patient, Doctor, PatientDoctorMapping

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'phone', 'email', 'created_at']
    search_fields = ['name', 'specialization']
    list_filter = ['specialization', 'created_at']
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'user', 'created_at']
    search_fields = ['name', 'user__username']
    list_filter = ['gender', 'age', 'created_at']
    
@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'assigned_date']
    search_fields = ['patient__name', 'doctor__name']
    list_filter = ['assigned_date']       

