#Use this calls to build out the associate class and ID's
import csv
import pandas as pd
import sys

# Add a function to get employee info by ID
def get_employee_by_id(pin):
    new_list = load_data('database/Employee.csv')  # Load employee data from CSV file
    for row in new_list:  # Iterate through each row in the employee list
        if len(row) > 0 and str(row[0]) == str(pin):  # Check if the row is not empty and the ID matches
            return {
                'id': row[0],  # Employee ID
                'first_name': row[1] if len(row) > 1 else None,  # First name if available
                'last_name': row[2] if len(row) > 2 else None,  # Last name if available
                'job_title': row[4] if len(row) > 4 else None,  # Job title if available
            }
    return None  # Return None if no match is found

#Validate the associate ID VS there job level => the main.py to validate before menu interaction
#include job_level and Skill_level




#load_date function to read the employee.csv file to upload in my_list array to store each variable row and pulled later in new_list[]
def load_data(filename):
    my_list = []  # Initialize an empty list to store rows
    with open (filename) as identify:       # Open the filepath to the specified CSV file
        identify_data = csv.reader(identify)  # Create a CSV reader object

        try:
            next(identify_data) # Skip the header information
            for row in identify_data:
               my_list.append(row)  # Append each row to the list
               
        except StopIteration:
            print("List is empty, StopIteration caught.")  # Handle empty file
            return []
    return my_list  # Return the list of rows

new_list = load_data('database/Employee.csv')  #calls load_data function to store the data in a list


def id_validate():
    id = input("Enter your personel ID: ")  # Prompt user to enter their personnel ID
    try:
        pin = int(id)  # Try to convert the input to an integer
    except ValueError:
        print("Invalid input. Please enter a valid number.")  # Handle invalid input
    # Assuming the pin is in the first column (index 0) of each row
    found = False  # Flag to track if the employee is found
    associate_id = None  # Initialize associate_id
    first_name = None  # Initialize first_name
    last_name = None  # Initialize last_name
    job_title = None  # Initialize job_title

    if new_list is None or not new_list:
        print("Employee list is empty. Please check the Employee.csv file.")  # Handle empty employee list
        return None, None, None, None
    
    for row in new_list:  # Check each row in the employee list
        if len(row) > 0 and str(row[0]) == str(pin):  # If the row is not empty and the ID matches
            found = True  # Set found flag to True
            associate_id = int(row[0])  # Get associate ID
            first_name = row[1] if len(row) > 1 else None   # Get first name (index 1)
            last_name = row[2] if len(row) > 2 else None    # Get last name (index 2)
            job_title = int(row[4])     # Get job title (index 4)
            if pin == associate_id:
                print(f"Name: {first_name} {last_name} ID: {associate_id}") # Print associate name and ID
                print(f"Employee has now been clocked in.")  # Confirm clock-in
            else:
                print("Pin (Employee ID) not found in employee list.")  # Handle mismatch
                print("Retry employee Identification number without any zeros.")
        
    if not found:
        print("Employee ID not found.")  # Handle not found case
    
    return associate_id, first_name, last_name, job_title  # Return employee info
    associate_id, first_name, last_name, job_title = id_validate()  # (Unreachable, can be removed)
# information that needs to be pushed to main.py
