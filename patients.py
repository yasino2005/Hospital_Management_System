import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog
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
    

#front end
class PatientApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Hospital Patient Management")
        self.root.geometry("950x550")
        self.root.configure(bg="#E8F6F3")  
        
        # Style للـ Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("Treeview", font=("Arial", 11), rowheight=30)
        style.configure("TButton", font=("Arial", 11, "bold"), padding=5)
        style.configure("TLabel", font=("Arial", 11))
        style.configure("TEntry", font=("Arial", 11))
        
        # Frame لإدخال بيانات المريض
        self.frame_input = tk.Frame(root, bg="#E8F6F3")
        self.frame_input.pack(pady=15)
        
        # Labels و Entry لكل خاصية
        tk.Label(self.frame_input, text="First Name", bg="#E8F6F3").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.frame_input, text="Last Name", bg="#E8F6F3").grid(row=0, column=2, padx=5, pady=5)
        tk.Label(self.frame_input, text="Email", bg="#E8F6F3").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.frame_input, text="Age", bg="#E8F6F3").grid(row=1, column=2, padx=5, pady=5)
        tk.Label(self.frame_input, text="Accommodation", bg="#E8F6F3").grid(row=2, column=0, padx=5, pady=5)
        
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.accommodation_var = tk.StringVar()
        
        tk.Entry(self.frame_input, textvariable=self.first_name_var, width=20, font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=5)
        tk.Entry(self.frame_input, textvariable=self.last_name_var, width=20, font=("Arial", 12)).grid(row=0, column=3, padx=5, pady=5)
        tk.Entry(self.frame_input, textvariable=self.email_var, width=20, font=("Arial", 12)).grid(row=1, column=1, padx=5, pady=5)
        tk.Entry(self.frame_input, textvariable=self.age_var, width=20, font=("Arial", 12)).grid(row=1, column=3, padx=5, pady=5)
        tk.Entry(self.frame_input, textvariable=self.accommodation_var, width=20, font=("Arial", 12)).grid(row=2, column=1, padx=5, pady=5)
        
        # Buttons
        self.frame_buttons = tk.Frame(root, bg="#E8F6F3")
        self.frame_buttons.pack(pady=10)
        
        tk.Button(self.frame_buttons, text="Add Patient", width=15, bg="#5DADE2", fg="white", command=self.add_patient).grid(row=0, column=0, padx=5)
        tk.Button(self.frame_buttons, text="Update Selected", width=15, bg="#F4D03F", fg="white", command=self.update_patient).grid(row=0, column=1, padx=5)
        tk.Button(self.frame_buttons, text="Delete Selected", width=15, bg="#E74C3C", fg="white", command=self.delete_patient).grid(row=0, column=2, padx=5)
        tk.Button(self.frame_buttons, text="Search", width=15, bg="#58D68D", fg="white", command=self.search_patient).grid(row=0, column=3, padx=5)
        tk.Button(self.frame_buttons, text="Show All", width=15, bg="#A569BD", fg="white", command=self.show_all_patients).grid(row=0, column=4, padx=5)
        
        # Treeview لعرض المرضى
        self.tree = ttk.Treeview(root, columns=("ID","First Name","Last Name","Email","Age","Accommodation"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("First Name", text="First Name")
        self.tree.heading("Last Name", text="Last Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Accommodation", text="Accommodation")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        # Bind لاختيار الصف
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        
        # عرض كل المرضى عند البداية
        self.show_all_patients()
