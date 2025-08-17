

## importing necessary libraries
import mysql.connector


## this is the connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)


## creating a function that adds an employee to the database##
def add_employee (Employee_ID, Job_TitleID, F_Name, L_Name, Hire_Date,PhoneNumber, Email, ManagerID):
    job_TitleID = input("Enter Job Title ID: ")
    F_Name = input("Enter First Name: ")
    L_Name = input("Enter Last Name: ")
    Hire_Date = input("Enter Hire Date (YYYY-MM-DD): ")
    PhoneNumber = input("Enter Phone Number: ")
    Email = input("Enter Email: ")
    ManagerID = input("Enter Manager ID (or leave blank if none): ")    
    Employee_ID = input("Enter Employee ID: ")
    cursor.execute("INSERT INTO Employee (EmployeeID, Job_TitleID, F_Name, L_Name, Hire_Date, PhoneNumber, Email, ManagerID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (Employee_ID, Job_TitleID, F_Name, L_Name, Hire_Date, PhoneNumber, Email, ManagerID))
    print(f"Employee {F_Name} {L_Name} added successfully.")
    mydb.commit()
    cursor.close()
    mydb.close()

## creating a function that removes an employee from the database##
def remove_employee(Employee_ID, F_Name,L_Name, Hire_Date, PhoneNumber, Email, ManagerID):
    Employee_ID = input("Enter employee id to remove:")
    F_Name = input("Enter First Name: ")
    L_Name = input("Enter Last Name: ")
    Hire_Date = input("Enter Hire Date (YYYY-MM-DD): ")
    PhoneNumber = input("Enter Phone Number: ")
    Email = input("Enter Email: ")
    ManagerID = input("Enter Manager ID (or leave blank if none): ")
    cursor.execute("DELETE FROM Employee WHERE EmployeeID = (Employee_ID, F_Name, L_Name, Hire_Date, PhoneNumber, Email, ManagerID) VALUES (%s, %s, %s, %s, %s, %s, %s)", (Employee_ID, F_Name, L_Name, Hire_Date, PhoneNumber, Email, ManagerID))
    print(f"Employee {F_Name} {L_Name} with ID {Employee_ID} has been removed successfully.")
    mydb.commit()
    cursor.close()
    mydb.close()


def check_out(Employee_ID,F_Name, L_Name, Date, Equipment_ID, Equipment_Name):
    Employee_ID = input("Enter Employee ID: ")
    F_Name = input("Enter First Name: ")
    L_Name = input("Enter Last Name: ")
    Date = input("Enter Date (YYYY-MM-DD): ")
    Equipment_ID = input("Enter Equipment ID: ")
    Equipment_Name = input("Enter Equipment Name: ")
    cursor.execute("UPDATE Equipment SET Status = 'Checked Out' WHERE EquipmentID = %s", (Equipment_ID,))
    cursor.execute("INSERT INTO Equipment_Checkout (EmployeeID, F_Name, L_Name, Date, EquipmentID, Equipment_Name) VALUES (%s, %s, %s, %s, %s, %s)", (Employee_ID, F_Name, L_Name, Date, Equipment_ID, Equipment_Name))  
    print(f"{F_Name} {L_Name} has checked out {Equipment_Name} on {Date}.")
    mydb.commit()
    cursor.close()
    mydb.close()



##value1 = input("Please verify your EmployeeID: ")
##value2 = input("Enter Clock-in Date/Time as YYYY-MM-DD hh:mm:ss: ")
##cursor.execute("INSERT INTO Clock (EmployeeID, Clock_In) VALUES (%s, %s)", (("value1, "value2"))
## print((f"Employee {EmployeeID} clocked in at {Clock_in}.")
##mydb.commit()
##cursor.close()?

# Clock Out
##value1 = input("Please verify your EmployeeID: ")
##value2 = input("Enter Clock-Out Date/Time as YYYY-MM-DD hh:mm:ss: ")
##cursor.execute("INSERT INTO Clock (EmployeeID, Clock_Out) VALUES (%s, %s)", ("value1, "value2"))
    ##print((f"Employee {EmployeeID} clocked in at {Clock_in} and clocked out at {clock_out}. If this is incorrect please see your supervisor for further action.")
##mydb.commit()
##cursor.close()
# Close the database connection
##mydb.close()