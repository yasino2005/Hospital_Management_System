import sqlite3
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
    

class Connect_To_db:
    ## connect to database
    @staticmethod
    def connect():
       con = sqlite3.connect('database.db')
    #    conect Foreign Keys
       con.execute("PRAGMA foreign_keys = ON")
       return con
   
class servicesPatient:
    # create table Patients
    @staticmethod
    def create_tables_Patients():
        con = Connect_To_db.connect()
        cursor = con.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            age INTEGER,
            accommodation TEXT
        )
        ''')
        con.commit()
        con.close()
        
# Add a Patient to the database 
    @staticmethod
    def add_patient(pat:Patient):
           con = Connect_To_db.connect()
           c=con.cursor()
           c.execute("""
            INSERT INTO Patients (first_name, last_name, email, age, accommodation) VALUES (?, ?, ?, ?, ?)""",(pat.first_name,pat.last_name,pat.email,pat.age,pat.accommodation) 
            )
           con.commit()
           con.close()