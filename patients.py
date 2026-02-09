import sqlite3
class Patient:
    def __init__(self,first_name,last_name,email,age,accommodation):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.accommodation=accommodation
    def __str__(self):
        return f"Patient : {self.first_name},{self.last_name},{self.email},{self.age},{self.accommodation} "
    

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
           
# get all patient from database
    @staticmethod 
    def get_Patient():
        con=Connect_To_db.connect()
        c=con.cursor()
        c.execute("SELECT * FROM Patients")
        lst_std=c.fetchall()
        con.close()
        return lst_std

# get patient from databse by id
    @staticmethod 
    def get_patientByid(id):
        con=Connect_To_db.connect()
        c=con.cursor()
        c.execute("SELECT * FROM Patients WHERE patient_id = ?",(id,))
        lst_std=c.fetchone()
        con.close()
        return lst_std

@staticmethod 
def get_patientBy_any(value):
    con = Connect_To_db.connect()
    c = con.cursor()
    value_like = f"%{value}%"
    
    c.execute("""
        SELECT * FROM Patients 
        WHERE patient_id = ? 
        OR first_name LIKE ? 
        OR last_name LIKE ? 
        OR email LIKE ? 
        OR CAST(age AS TEXT) LIKE ? 
        OR accommodation LIKE ?
    """, (value, value_like, value_like, value_like, value_like, value_like))
    
    std = c.fetchall()
    con.close()    
    return std

 #  delete patient from database by id
    @staticmethod
    def delete_patientByid(id):
       con=Connect_To_db.connect()
       c=con.cursor()
       c.execute("DELETE FROM  Patients WHERE patient_id=?",(id,))
       con.commit()
       con.close()
       
# update patients from database by id
    @staticmethod
    def update_patientByid(id,first_name,last_name,email,age,accommodation):
         con= Connect_To_db.connect()
         c=con.cursor()
         c.execute("UPDATE Patients SET first_name =? , last_name = ?,email=? ,age=?,accommodation=? WHERE patient_id=?  ",(first_name,last_name,email,age,accommodation ,id))
         con.commit()
         con.close()
    
