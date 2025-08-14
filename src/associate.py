#Use this calls to build out the associate class and ID's
import csv
import pandas as pd
import sys

# Add a function to get employee info by ID
def get_employee_by_id(pin):
    new_list = load_data('database/Employee.csv')
    for row in new_list:
        if len(row) > 0 and str(row[0]) == str(pin):
            return {
                'id': row[0],
                'first_name': row[1] if len(row) > 1 else None,
                'last_name': row[2] if len(row) > 2 else None
            }
    return None

#Validate the associate ID VS there job level => the main.py to validate before menu interaction
#include job_level and Skill_level




#load_date function to read the employee.csv file to upload in my_list array to store each variable row and pulled later in new_list[]
def load_data(filename):
    my_list = []
    with open (filename) as identify:       #opens the filepath to whatever csv file
        identify_data = csv.reader(identify)
        next(identify_data) #skips the header information

        for row in identify_data:
            my_list.append(row)
        return my_list


new_list = load_data('database/Employee.csv')  #calls load_data function to store the data in a list


def id_validate():
    id = input("Enter your personel ID: ")  # Example pin, replace with actual value as needed
    pin = int(id)
    # Assuming the pin is in the first column (index 0) of each row
    found = False
    associate_id = None
    first_name = None
    last_name = None
    for row in new_list:                                    #checking each row
        if len(row) > 0 and str(row[0]) == str(pin):
            found = True
            associate_id = row[0]
            first_name = row[1] if len(row) > 1 else None   #index 1 of the csv file 
            last_name = row[2] if len(row) > 2 else None    #index 2 of the csv file
            print(f"Name: {first_name} {last_name} ID: {associate_id}") #printing the associate name and id
            print(f"Employee has now been clocked in.")
        else:
            print("Pin (Employee ID) not found in employee list.")
            print("Retry employee Identification number without any zeros.")
            sys.exit() #to force quit the application if the pin doesn't match any ID 
             
    return associate_id, first_name, last_name
    associate_id, first_name, last_name = id_validate()
# information that needs to be pushed to main.py
def tool():
    pass