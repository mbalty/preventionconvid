from enum import Enum

class Collections():
    USERS = 'users'
    LOCATIONS = 'locations'
    
class USER_ROLE():
    DOCTOR = "doctor"
    PATIENT = "patient"

ACTIVATION_MAIL = 'http://localhost:5000/api/v1/users/activate/{id}'
