class Patient:
    count_patient_id=0
    def __init__(self,first_name,last_name,email,age,accommodation):
        Patient.count_student_id+=1
        self.patient_id= Patient.count_student_id
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.accommodation=accommodation
    def __str__(self):
        return f"Patient : {self.count_student_id},{self.first_name},{self.last_name},{self.email},{self.age},{self.accommodation} "
    

