from django.db import models

class PatientReport(models.Model): 
    patient_id = models.CharField(db_index = True, max_length = 20, unique = True)
    patient_name = models.CharField(max_length = 100)
    patient_phone = models.CharField(max_length=15)
    test_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length = 100, default = "Unassigned")

    verdict = models.TextField(default= "Pending")

    is_reviewed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Report {self.patient_id} - {self.patient_name}"