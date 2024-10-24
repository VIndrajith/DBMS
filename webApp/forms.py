from django import forms

from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
    p_id = forms.IntegerField(
        label = 'Patient ID',
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        ),
        min_value = 0
    )

    name = forms.CharField(
        max_length=20,
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control',}
        )
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        ),
        min_value = 0
    )

    gender  = forms.CharField(
        label='Gender',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    address = forms.CharField(
        max_length=30,
        label='Address',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['appointment', 'diagnosis', 'med']
        widgets = {
            'diagnosis': forms.TextInput(attrs={'class': 'form-control'}),
            'med': forms.TextInput(attrs={'class': 'form-control'}),
        }