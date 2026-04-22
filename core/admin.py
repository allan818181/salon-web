from django.contrib import admin
from .models import Appointment, JobApplication, Contact

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'service', 'appointment_date', 'status', 'created_at')
    list_filter = ('status', 'service', 'appointment_date')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    ordering = ('-created_at',)

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'position', 'status', 'created_at')
    list_filter = ('status', 'position')
    search_fields = ('full_name', 'email', 'phone')
    ordering = ('-created_at',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)