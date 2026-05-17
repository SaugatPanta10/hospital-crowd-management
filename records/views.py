from django.shortcuts import render # django.shortcuts is a module that provides useful tools like rendering HTML templates , and render is a function used to return HTML pages
from django.http import HttpResponse #django.http is a module that handles web requests and responses. HttpResponse sends text babck to the browser 

# Create your views here.
def home_view(request):  #request is an object that contains the information sent by the browser to Django such as URL, user data,
    return render(request, 'records/home.html')

def doctor_dashboard_view(request):
    return render(request, 'records/doctor_dashboard.html')

