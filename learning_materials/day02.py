patient_name = "Hari Maya Shrestha"
report_status = "Reviewed"

print ("--- Welcome to the Patient Portal ---")

if report_status == "Reviewed":
    print (f"Hello {patient_name}, you doctor has submitted your verdict. ")
    print ("Action: You can view it online now. DO NOT come to the hospital.") 

elif report_status == "In Progress": 
    print (f"Hello {patient_name}, your lab samples are currently being tested.")
    print ("Action: Please check back in few hours.")

else: 
    print (f"Hello {patient_name}, your report is pending in the queue.")
    print ("Action: Please wait. We will notify you via SMS.")


# """this is a challenge task"""

# user_role = "doctor"

# if user_role == "doctor":
#     print ("Redirecting to Doctor Dashboard... [Review Pending Reports]")

# elif user_role == "lab_tech": 
#     print ("Redirecting to Lab Dashboard.. [UPload New PDF Reports]")

# elif user_role == "patient":
#     print ("Redirecting to Patient Portal.. [Enter Patient ID]")

# else: 
#     print("Access Denied: Invalid Role") 
