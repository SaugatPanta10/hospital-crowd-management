hospital_name = "Bir Hospital"
total_beds = 500 

patient_report = {
    "patient_id" : 101, 
    "patient_name": "Ram Bahadur", 
    "test_name": "Blood Sugar", 
    "verdict": "Pending", 
    "is_reviewed": False
}

print("Hospital: " + hospital_name)
print ("Patient Name: " + patient_report["patient_name"])
print("Test Statu: " + patient_report["verdict"])

"""this was a challenge task
"""
# lab_technician = "Chandra Bhandari" 
# patient_report["verdict"] = "Normal levels. No lifestyle changes needed."
# patient_report["is_reviewd"]= True

# print("/n ---- Updated Report Summary-----")
# print("Verified By: " + lab_technician)
# print("Final Verdict: " + patient_report["verdict"])
# print("Is Report Reviewed?" + str (patient_report["is_reviewed"]))