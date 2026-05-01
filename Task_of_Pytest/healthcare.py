class PatientValidationError(Exception):
    "Custom exception for invalid patient data"
    pass
def validate_patient(age,heart_rate):
    if not (20<=heart_rate<=220):
        raise PatientValidationError("Heart Rate should br between 20 to 220")
    elif not (0<=age<=120):
        raise PatientValidationError("Invalid Patient Age .Must be between 0 and 120 ")
    return True