import pytest
from healthcare import validate_patient
from healthcare import PatientValidationError

def test_valid_patient_data():
    assert validate_patient(22,80)
 
def test_invalid_age():
    with pytest.raises(PatientValidationError,match="Invalid Patient Age .Must be between 0 and 120"):
        validate_patient(130,90)
        
def test_invalid_heart_rate():
    with pytest.raises(PatientValidationError,match="Heart Rate should br between 20 to 220"):
        validate_patient(90,320)