from django.shortcuts import render # django.shortcuts is a module that provides useful tools like rendering HTML templates , and render is a function used to return HTML pages
from django.http import HttpResponse #django.http is a module that handles web requests and responses. HttpResponse sends text babck to the browser 

# Create your views here.
def home_view(request):
    return HttpResponse("Welcome to UpacharVerdict: The Hospital Crowd Management System. ")

def doctor_dashboard_view(request):
    return HttpResponse("Doctor Dashboard. You have 3 pending reports to review.") 