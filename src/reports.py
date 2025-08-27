import csv
import loaders
import pandas as pd
from loaders import EQUIPMENT_FILE, MATERIAL_LOC_FILE
import time

#CSV reader
def load_data(filename):
    my_list = []
    with open (filename, 'r') as identify:       #opens the filepath to whatever csv file
        identify_data = csv.reader(identify)
        next(identify_data) #skips the header information

        for row in identify_data:
            my_list.append(row)
        return my_list
#reports function loader

#Auditor Function
def auditor_report(): # done
    while True:
        time.sleep(1)
        print("===| Auditor Reports |===")
        print("1.  Inventory By Employee")
        print("2.  Inventory By Condition")
        print("3.  Inventory By Tool Room")
        print("4.  Inventory By Materials")

        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                loaders.inventory_employee_tool(EQUIPMENT_FILE)
            elif input_value == '2':
                loaders.inventory_condition_tool(EQUIPMENT_FILE)
            elif input_value == '3':
                loaders.inventory_tool_room(EQUIPMENT_FILE)
            elif input_value == '4':
                loaders.inventory_materials(MATERIAL_LOC_FILE)
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 




def reports_menu(): # done
    while True:
        time.sleep(1)
        print("===| Reports |===")
        print("1.  Inventory By Employee")
        print("2.  Inventory By Condition")
        print("3.  Inventory By Tool Room")
        print("4.  Inventory By Materials")

        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                loaders.inventory_employee_tool(EQUIPMENT_FILE)
            elif input_value == '2':
                loaders.inventory_condition_tool(EQUIPMENT_FILE)
            elif input_value == '3':
                loaders.inventory_tool_room(EQUIPMENT_FILE)
            elif input_value == '4':
                loaders.inventory_materials(MATERIAL_LOC_FILE)
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 



def live_reports(): # done

    associate_id = None
    first_name = None
    last_name = None
    new_list = load_data('database/Employee.csv')
    for row in new_list:
        if len(row) > 0:
            found = True
            associate_id = int(row[0])
            first_name = row[1] if len(row) > 1 else None   #index 1 of the csv file 
            last_name = row[2] if len(row) > 2 else None 
            print("Employee ID, first name,    Last name")
            print(f"{associate_id}   {first_name}     {last_name}")
    
  
    
def email_report(): # pending
    print("")

