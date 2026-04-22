from django.db import models
from django.utils import timezone

SERVICE_CHOICES = [
    ('haircut', 'Hair Cutting & Styling'),
    ('coloring', 'Hair Coloring'),
    ('extensions', 'Hair Extensions'),
    ('eyelash', 'Eyelash Extensions'),
    ('eyebrow', 'Semi-Permanent Eyebrow'),
    ('makeup', 'Makeup'),
    ('bridal', 'Bridal Services'),
    ('spa', 'Spa & Massage'),
    ('other', 'Other'),
]

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
]

POSITION_CHOICES = [
    ('senior_stylist', 'Senior Stylist'),
    ('junior_stylist', 'Junior Stylist'),
    ('spa_therapist', 'Spa Therapist'),
    ('lash_brow', 'Lash & Brow Specialist'),
    ('receptionist', 'Receptionist'),
    ('makeup_artist', 'Makeup Artist'),
]

class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    additional_details = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_service_display()}"
    
    class Meta:
        ordering = ['-created_at']

class JobApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    experience = models.TextField()
    why_join = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.get_position_display()}"
    
    class Meta:
        ordering = ['-created_at']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        ordering = ['-created_at']