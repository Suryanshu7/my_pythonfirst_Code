import psycopg2

# CONNECT TO THE DATABASE 
def database():
    conn = psycopg2.connect(
        
        host = "localhost", #Employee_Management_System
        database = "employee_management_system",
        user = "postgres",
        password = "demo123",
        port = "5432",
    )

    # CREATE A TABLE 
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Employee_Management(employee_id INT  PRIMARY KEY,
            employee_Name text,
            gender text,
            date_of_birth date,
            mobile_number varchar(12),
            department text,
            salary int);"""
    )
    conn.commit()
    print("Table created successfully!")

    cursor.close()
    conn.close()



database()

# Insert data 
def insert_data():
    conn = psycopg2.connect(
        host ="localhost",
        port = "5432",
        user = "postgres",
        password = "demo123",
        database = "employee_management_system"
    )
    
    cursor = conn.cursor()
    while True:
            add_data = input("Add  Data?(YES/NO):")
            if add_data.lower()!="yes":
                    break
            employee_id = int(input("Enter Your Employee Id: "))
            employee_Name  = input("Enter Your Full Name: ")
            gender = input("Enter Your Gender: ")
            date_of_birth = input("Enter your DATE OF BIRTH: ")
            mobile_number = input("Enter your Mobile Number: ")
            department = str(input("Enter Your Department: "))
            salary= int(input("Enter your Salary: "))

            try:
                cursor.execute("""INSERT INTO Employee_Management(employee_id,employee_Name,gender,date_of_birth,mobile_number,department,salary) VALUES(%s,%s,%s,%s,%s,%s,%s)""",
                                (employee_id,employee_Name,gender,date_of_birth,mobile_number,department,salary)
                )
    
                conn.commit()

            except psycopg2.errors.UniqueViolation:
                conn.rollback()
                print(" Employee ID already exists. Please enter another ID.")
            choice = input("Add More Data?(YES/NO):")
            if choice.lower()!="yes":
                break
    print("Data insert succesfully")


     
            
    conn.close()
    cursor.close()
insert_data()

def show_data():
    conn= psycopg2.connect(
        dbname="employee_management_system",
        user="postgres",
        password="demo123",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM Employee_Management")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()    
    conn.close()

show_data()  

def search_data():
    conn= psycopg2.connect(
        dbname="employee_management_system",
        user="postgres",
        password="demo123",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    emp_id = int(input("Enter Your Employee ID: "))
    cursor.execute("select*from Employee_Management WHERE employee_id=%s;",
                   (emp_id,))
    Show = cursor.fetchone()
    print(Show)

    print("wait we are checking")
    conn.commit()
    print(f"This is a searching data:{emp_id}")
    cursor.close()
    conn.close()

search_data()

"""def delete_table():
    conn= psycopg2.connect(
        dbname="employee_management_system",
        user="postgres",
        password="demo123",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    dele = int(input("Delete a Employee record give Emp_ID: "))
    cursor.execute("DELETE  FROM Employee_Management WHERE employee_id=%s;",
                   (dele,)
                   )
    conn.commit()
    print(f"Deleted employee_id {dele} records")
    #check_data = int(input("show_data. Yes or No?: "));
    #if check_data.lower()!="yes":
    print(show_data)   
    cursor.close()
    conn.close()
delete_table()"""
def truncate_table():
    conn= psycopg2.connect(
             dbname="employee_management_system",
             user="postgres",
             password="demo123",
             host="localhost",
             port="5432"
         )
     
    cursor = conn.cursor()

    traun = input("Can You Trauncate this Table? YES or NO?: ")
    if traun.lower()=="yes":
        cursor.execute("TRUNCATE TABLE Employee_Management;")
        conn.commit()
        print("Table Truncate Succesfully.")
    else:
        print("Table was not Truncate")
    cursor.close()
    conn.close()
truncate_table()