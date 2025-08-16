# Clock In
value1 = input("Please verify your EmployeeID: ")
value2 = input("Enter Clock-in Date/Time as YYYY-MM-DD hh:mm:ss: ")
cursor.execute("INSERT INTO Clock (EmployeeID, Clock_In) VALUES (%s, %s)", ("value1, "value2"))
    print((f"Employee {EmployeeID} clocked in at {Clock_in}.")
mydb.commit()
cursor.close()

# Clock Out
value1 = input("Please verify your EmployeeID: ")
value2 = input("Enter Clock-Out Date/Time as YYYY-MM-DD hh:mm:ss: ")
cursor.execute("INSERT INTO Clock (EmployeeID, Clock_Out) VALUES (%s, %s)", ("value1, "value2"))
    print((f"Employee {EmployeeID} clocked in at {Clock_in} and clocked out at {clock_out}. If this is incorrect please see your supervisor for further action.")
mydb.commit()
cursor.close()
