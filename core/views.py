from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils import translation
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from .models import Appointment, JobApplication, Contact

def home(request):
    return render(request, 'core/home.html')

def services(request):
    return render(request, 'core/services.html')

def menu(request):
    return render(request, 'core/menu.html')

def gallery(request):
    return render(request, 'core/gallery.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        date = request.POST.get('date')
        time_hour = request.POST.get('hour')
        time_minute = request.POST.get('minute')
        period = request.POST.get('period')
        message = request.POST.get('message')
        
        from datetime import datetime, time as dt_time
        try:
            hour_val = int(time_hour)
            if period == 'PM' and hour_val != 12:
                hour_val += 12
            elif period == 'AM' and hour_val == 12:
                hour_val = 0
            time_obj = dt_time(hour_val, int(time_minute))
        except:
            time_obj = dt_time(10, 0)
        
        appointment = Appointment.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            service=service,
            appointment_date=date,
            appointment_time=time_obj,
            additional_details=message
        )
        
        messages.success(request, f'Thank you {first_name}! Your appointment has been booked successfully. We will contact you at {phone} to confirm.')
        return redirect('contact')
    
    return render(request, 'core/contact.html')

def join(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')
        experience = request.POST.get('experience')
        why = request.POST.get('why')
        
        application = JobApplication.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            position=position,
            experience=experience,
            why_join=why
        )
        
        messages.success(request, f'Thank you {full_name}! Your application has been submitted successfully. We will review and contact you if shortlisted.')
        return redirect('join')
    
    return render(request, 'core/join.html')

def set_language(request, lang):
    # Activate the language
    translation.activate(lang)
    
    # Get the next page from query string or default to home
    next_page = request.GET.get('next', '')
    if not next_page:
        next_page = '/'
    
    # Set language in session
    request.session['_language'] = lang
    
    response = redirect(next_page)
    response.set_cookie('django_language', lang, max_age=60*60*24*365)
    return response