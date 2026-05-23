from django import forms
from .models import PatientReport

class PatientReportForm(forms.ModelForm):
    class Meta:
        model = PatientReport
        # Only these fields will show up on the HTML page
        fields = ['patient_id', 'patient_name', 'patient_phone', 'test_name']

class DoctorVerdictForm(forms.ModelForm):
    class Meta: 
        model = PatientReport
        fields = ['doctor_name', 'verdict', 'is_reviewed']