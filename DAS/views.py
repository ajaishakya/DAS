
from django.shortcuts import redirect, render

def index(request):
    return render(request,'main/index.html')

def DOCTOR_DASHBOARD(request):
    return render(request,'main/doctor-dashboard.html')

def APPOINTMENTS(request):
    return render(request,'main/appointments.html')

def login(request):
    return render(request,'main/login.html')