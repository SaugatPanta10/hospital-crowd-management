from django import forms
from .models import PatientReport

class PatientReportForm(forms.ModelForm):
    class Meta:
        model = PatientReport
        # Only these fields will show up on the HTML page
        fields = ['patient_id', 'patient_name', 'verdict']

class DoctorVerdictForm(forms.ModelForm):
    class Meta: 
        model = PatientReport
        # FIXED: A doctor updating a report only needs to modify the verdict text block
        fields = ['verdict']