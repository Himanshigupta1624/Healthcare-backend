from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    phone=models.CharField(max_length=15,blank=True)
    email=models.EmailField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} -{self.specialization}"
    

class Patient(models.Model):
    GENDER_CHOICES=[
        ("M","Male"),
        ("F","Female"),
        ("O",'Other')
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    phone=models.CharField(max_length=15,blank=True)
    address=models.TextField(blank=True,null=True)
    medical_history=models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.age} years old"
    
    

class PatientDoctorMapping(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='doctor_mappings')
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='patient_mappings')   
    assigned_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        unique_together = ('patient', 'doctor')
    
    def __str__(self):
        return f"{self.patient.name} -> {self.doctor.name}"    
