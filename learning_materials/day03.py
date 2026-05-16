patient_queue = [
    {"id": 101, "name": "Ram Bahadur", "status": "Pending"}, 
    {"id": 102, "name": "Sita Thapa", "status": "Reviewed"}, 
    {"id": 103, "name": "Gopal Sharma","status": "Pending" }
]

print ("--- Current Patient Queue Status ----")

for patient in patient_queue: 
    print (f"Patient ID: {patient['id']} | {patient['name']} | Status: {patient['status']}")


""" this is a challenge task"""

# for patient in patient_queue: 
#     if patient['status'] == "Pending":
#         print (f"ATTENTION: Doctor review needed for {patient['name']} ")

#     else: 
#         print("skip")