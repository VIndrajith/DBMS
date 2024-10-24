from django.shortcuts import render,redirect
from .models import Appointment, Patient, Doctor
from .forms import *

# Create your views here.
def main(request):
    return render(request,"main.html")

def patient(request):
    return render(request,'patient.html')

def auth(request):
    return render(request,'auth.html')

def appoint(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(patient)
    else:
        form = AppointmentForm()
    return render(request, 'app_book.html', {'form': form})

def applist(request):
    appoint = Appointment.objects.all()
    return render(request,"app_list.html",{'appointments':appoint})

def patientd(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book/')
    else:
        form = PatientForm()
    return render(request, 'patient_details.html', {'form': form})

def treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(auth)
    else:
        form = TreatmentForm()
    return render(request, 'treatment.html', {'form': form})

def treatH(request):
    treat = Treatment.objects.all()
    return render(request,"treatH.html",{'treatments':treat})