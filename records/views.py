from django.shortcuts import render, get_object_or_404, redirect # django.shortcuts is a module that provides useful tools like rendering HTML templates , and render is a function used to return HTML pages
from django.http import HttpResponse #django.http is a module that handles web requests and responses. HttpResponse sends text babck to the browser 
from .models import PatientReport
from .models import PatientReport
from .forms import PatientReportForm, DoctorVerdictForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home_view(request):  #request is an object that contains the information sent by the browser to Django such as URL, user data,
    total_patients = PatientReport.objects.count()
    context = {
        'patients': total_patients
        }
    return render(request, 'records/home.html', context)

def patient_detail_view(request, patient_id):
    report = get_object_or_404(PatientReport, patient_id=patient_id)
    context = {
        'report' : report
    }
    return render(request, 'records/patient_detail.html', context)
    
def update_verdict_view (request, patient_id):
    report = get_object_or_404(PatientReport, patient_id = patient_id)

    if request.method =='POST':
        form = DoctorVerdictForm(request.POST, instance = report)
        if form.is_valid():
            form.save()
            messages.success(request, "new patient report created successfully")
            return redirect('doctor_dashboard')
        
    else:
        form = DoctorVerdictForm(instance = report)

    context = {'form': form, 'report': report}
    return render(request, 'records/update_verdict.html', context)

def home_view(request):
    search_query = request.GET.get('query')
    patient_result = None 

    if search_query:
        patient_result = PatientReport.objects.filter(patient_id=search_query).first()

    total_count = PatientReport.objects.count()

    context = {
        'total_patients': total_count, 
        'search_query': search_query, 
        'patient_result': patient_result
    }
    return render(request, 'records/home.html', context)

def delete_report_view(request, patient_id): 
    report = get_object_or_404(PatientReport, patient_id = patient_id)

    if request.method == 'POST':
        report.delete()
        messages.success(request, "New patient report created successfully")
        return redirect('doctor_dashboard')
    
    context = {'report': report}
    return render(request, 'records/delete_confirm.html', context)

@login_required
def doctor_dashboard_view(request):
    reports = PatientReport.objects.filter(doctor = request.user) 
    return render(request, 'records/doctor_dashboard.html', {'reports': reports}) #this context must always be a dictionary 

@login_required
def create_report_view(request):
    if request.method == 'POST':
        form = PatientReportForm (request.POST)
        if form.is_valid():
            report = form.save(commit = False)
            report.doctor = request.user
            report.save()
            messages.success(request, "New Patient report created successfully!")
            return redirect('doctor_dashboard')
           
    else:
        form = PatientReportForm
    return render(request, 'records/create_report.html', {'form': form})