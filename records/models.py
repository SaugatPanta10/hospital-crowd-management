from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User model

class PatientReport(models.Model):
    # Your existing fields
    patient_id = models.CharField(max_length=50, unique=True)
    patient_name = models.CharField(max_length=100)
    verdict = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='reports')

    def __str__(self):
        return f"{self.patient_name} ({self.patient_id})"