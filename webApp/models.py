from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    fee = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name} ({self.department})"

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'),('Other','Other')])
    phone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, default='Scheduled')

    def __str__(self):
        return f"{self.patient}"

class Treatment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='treatment')
    diagnosis = models.TextField()
    med = models.TextField()

    def __str__(self):
        return f"Treatment for {self.appointment.patient}"