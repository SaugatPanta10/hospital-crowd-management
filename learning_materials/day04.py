# def format_verdict (patient_name, test_name, verdict_text): 
#     formatted_msg = f" PATIENT: {patient_name} | TEST: {test_name} | VERDICT: {verdict_text}"
#     return formatted_msg

# name = "Gopal Sharma"
# test = "X-Ray"
# verdict = "Chest is clear. NO abnormalities detected."

# final_result = format_verdict(name, test, verdict)

# print ("--- System Generated Output ----")
# print (final_result)

""" this is challenge task"""
def send_sms_simulation(patient_phone, status):
    if status == "Reviewed":
        string_message = "Your doctor's verdict is ready online. Please check your portal."
    elif status == "Pending": 
        string_message = "Your report is received and in the queue."

    return f"[SMS SENT TO {patient_phone}: {string_message}"

patient_phone = 98654515121
status = "Pending"

result = send_sms_simulation(patient_phone, status)

print(result)