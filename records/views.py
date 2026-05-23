from django.shortcuts import render, get_object_or_404 # django.shortcuts is a module that provides useful tools like rendering HTML templates , and render is a function used to return HTML pages
from django.http import HttpResponse #django.http is a module that handles web requests and responses. HttpResponse sends text babck to the browser 
from .models import PatientReport
from django.shortcuts import render, get_object_or_404, redirect
from .models import PatientReport
from .forms import PatientReportForm

def home_view(request):  #request is an object that contains the information sent by the browser to Django such as URL, user data,
    total_patients = PatientReport.objects.count()
    context = {
        'patients': total_patients
        }
    return render(request, 'records/home.html', context)

def doctor_dashboard_view(request):
    all_reports = PatientReport.objects.all() #Take all records from PatientReport table and store them in a list
    context = {
        'reports': all_reports
        }
    return render(request, 'records/doctor_dashboard.html', context) #this context must always be a dictionary 

def patient_detail_view(request, patient_id):
    report = get_object_or_404(PatientReport, patient_id=patient_id)
    context = {
        'report' : report
    }
    return render(request, 'records/patient_detail.html', context)
    
def create_report_view(request):
    if request.method == 'POST':
        form = PatientReportForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        
    else:
        form = PatientReportForm

    context = {'form': form}
    return render(request, 'records/create_report.html', context)

def update_verdict_view (request, patient_id):
    report = get_object_or_404(PatientReport, patient_id = patient_id)

    if request.method =='POST':
        form = DoctorVerdictForm(request.POST, instance = report)
        if form.is_valid():
            form.save()
            return redirect('patient_detail', patient_id = report.patient_id)
        
    else:
        form = DoctorVerdictForm(instance = report)

    context = {'form': form, 'report': report}
    return render(request, 'records/update_verdict.html', context)