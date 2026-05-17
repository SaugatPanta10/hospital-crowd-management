from django.urls import path #django.urls is a module to handle URL routing in Django, path is a function used to define URL Patterns 
from . import views  # '.' means current folder, views means import views.py from the current folder

# this is the list of all URL routes in this app. 
urlpatterns = [ # it must be called exactly urlpatterns as this is a special django variable name 
    path('', views.home_view, name = 'home'),
    path('doctor/', views.doctor_dashboard_view, name = "doctor dashboard"),
    path('patient/<str:patient_id>/', views.patient_detail_view, name = 'patient_detail')
]