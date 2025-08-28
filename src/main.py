#main file for selection system
import time
import os
import loaders
import sys
import associate as assoc
import reports
from datetime import datetime

# File paths
CLOCK_FILE = "database/Clock.csv"
EMPLOYEE_FILE = "database/Employee.csv"
JOB_INFO_FILE = "database/JobInfo.csv"
EQUIPMENT_FILE = "database/Equipment.csv"
EMPLOYEE_CERT_FILE = "database/EmployeeCertification.csv"
LOCATION_FILE = "database/LocationsList.csv"
MATERIAL_LOC_FILE = "database/MaterialInventory.csv"
TRANSACTIONS_FILE = 'database/Transactions.csv'
WORK_ORDER_FILE = 'database/WorkOrder.csv'

#changed datetime to exclude miliseconds
original_datetime = datetime.now()
formatted_datetime = original_datetime.strftime('%m-%d-%Y \n%H:%M')


os.system('cls' if os.name == 'nt' else 'clear')

#defining the main UI 
def pull_menu(associate_id, first_name, last_name, job_title):
    
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print(f"Configuring Employee Job Type Menu for id {associate_id} ....")
        time.sleep(2)
        print(f"Taking you to {first_name} {last_name} menu")

        if job_title >= 0 and job_title <= 72:
            maintenance()
        elif job_title >= 73 and job_title <= 75:
            hr()
        elif job_title >= 76 and job_title <= 78:
            finance()
        elif job_title >= 79 and job_title <= 80:
            auditor()
        elif job_title >= 81 and job_title <= 84:
            safety()
        elif job_title >= 85 and job_title <= 90:
            project_manager()
        elif job_title >= 91 and job_title <= 93:
            administration()
        elif job_title >= 94 and job_title <= 95:
            procurement()
        elif job_title >= 96 and job_title <= 99:
            warehouse()
        elif job_title >= 100 and job_title <= 103:
            equipment()
        elif job_title >= 104 and job_title <= 108:
            info_tech()
        elif job_title >= 109 and job_title <= 112:
            other()
        elif job_title >= 113:
            print("\n Employee needs to seek HR. Please contact them right away.")
            time.sleep(3)
        else:
            print("\nInput cancelled or not available. Exiting program.")
            sys.exit()
# maintenance function done
def maintenance():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Maintenance |===")
        print("1.  Clock out")
        print("2.  Equipment Check In")
        print("3.  Equipment Check Out")
        print("4.  Employee Personal Equipment Inventory")
        input_value = None  # Initialize input_value to None
        try:
            input_value = input("Select an option: ")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break    
    if input_value == "1":
        print(f"{first_name} {last_name} has clocked out for the day.")
    elif input_value == "2":
        loaders.count_rows_trans(TRANSACTIONS_FILE)
        loaders.transactions(TRANSACTIONS_FILE)
        loaders.tool_location_update(EQUIPMENT_FILE)
        print (f"Please return your tools to the window clerk now")
    elif input_value == "3":
        print ("Select the tool room you are checking out from.")
        loaders.inventory_tool_room(EQUIPMENT_FILE)
        print ("The list generated is the tools available for check out.")
        loaders.count_rows_trans(TRANSACTIONS_FILE)
        loaders.transactions(TRANSACTIONS_FILE)
        loaders.tool_location_update(EQUIPMENT_FILE)
        print (f"Please grab your tools from the window clerk now")
    elif input_value == "4":
        loaders.inventory_employee_tool(EQUIPMENT_FILE)
    else:
        print("\nInput cancelled or not available. Exiting program.")


#HR function done
def hr():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| HR |===")
        print("1.  Clock Out")
        print("2.  Add Employee")
        print("3.  Remove Employee")
        print("4.  Update Employee information")
        input_value = None  # Initialize input_value
        try:
            input_value = input("Select an option: ")
            if input_value == '1':
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == "2":
                loaders.count_rows_csv(EMPLOYEE_FILE)
                print(f"Total employees: {loaders.count_rows_csv(EMPLOYEE_FILE)}")
                loaders.add_employee(EMPLOYEE_FILE)
            elif input_value == '3':
                loaders.remove_employee(EMPLOYEE_FILE)
            elif input_value == '4':
                print("Enter 0 to skip any field, unless otherwise noted.\n")
                loaders.update_employee()
            else:
                print("\nInput cancelled or not available. Exiting program.")
    
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    

#finance function done
def finance():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Finance |===")
        print("1.  Clock out")
        print("2.  Lost and Damage Equipment Report")
        print("3.  Equipment Price Checker")
        input_value = None  # Initialize input_value
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == '2':
                loaders.inventory_condition_tool(EQUIPMENT_FILE)
            elif input_value == '3':
                loaders.individual_equipment_price(EQUIPMENT_FILE)
            else:
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    
#Auditor function done
def auditor():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Auditor |===")
        print("1.  Clock out")
        print("2.  Generate All Reports")
        input_value = None  # Initialize input_value
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == '2':
                reports.auditor_report()
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
#Safety Function  pending functions 2 and 3
def safety(): #clayton
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Safety |===")
        print("1.  Clock out")
        print("2.  Certificate Employee Update") #Certificate update for empoyee
        print("3.  Certificate Equipment Update")#Certificate update for equipment
        input_value = None  # Initialize input_value
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == '2':
                loaders.certificate_employee()
            elif input_value == '3':
                loaders.certificate_equipment()
            else: 
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    pass
#Project manager function done
def project_manager():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Manager |===")
        print("1.  Clock out")
        print("2.  Generate All Reports")
        input_value = None  # Initialize input_value
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == '2':
                reports.reports_menu()
            else:
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    
#Administration function  pending function 3
def administration():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Admin |===")
        print("1.  Clock out")
        print("2.  Live Status Report")
        print("3.  Email report")
        input_value = None  # Initialize input_value
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == "2":
                reports.live_reports()
            elif input_value == "3":
                reports.email_report()
            else: 
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    
#Procurement Function done
def procurement():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Procurement |===")
        print("1.  Clock out")
        print("2.  Inventory Report")
        print("3.  Update Inventory tools/equipment")
        input_value = None  # Initialize input_value
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == "2":
                loaders.inventory_tool_room(EQUIPMENT_FILE)
            elif input_value == "3":
                print("Enter 0 to skip any field, unless otherwise noted.\n")
                loaders.update_inventory_tool(EQUIPMENT_FILE)
            else:    
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    
#Warehouse function done
def warehouse():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Warehouse |===")
        print("1.  Clock out")
        print("2.  Materials Update")
        print("3.  Inventory Report")
        input_value = None  # Initialize input_value
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input == '2':
                print("Enter 0 to skip any field, unless otherwise noted.\n")
                loaders.material_update()
            elif input == '3':
                loaders.inventory_materials(MATERIAL_LOC_FILE)
            else:
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 


#Equipment Function done
def equipment():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Tool Room |===")
        print("1.  Clock out")
        print("2.  Equipment Location Update")
        print("3.  Equipment Inventory")
        print("4.  Update Equipment Condition")
        input_value = None  # Initialize input_value
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input == '2':
                loaders.tool_location_update(EQUIPMENT_FILE)
            elif input == '3':
                loaders.inventory_tool_room(EQUIPMENT_FILE)
            elif input == '4':
                loaders.tool_condition_update(EQUIPMENT_FILE)
            else:
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 




#info_tech function done
def info_tech():
    while True:
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| IT |===")
        print("1.  Maintenance")
        print("2.  HR")
        print("3.  Finance")
        print("4.  Auditor/Compliance")
        print("5.  Safety")
        print("6.  Project Manager")
        print("7.  Administration")
        print("8.  Procurement")
        print("9.  Warehouse")
        print("10. Equipment")
        print("11. IT")
        print("12. Other")
        input_value = None  # Initialize input_value

        try:
            input_value = input("Select an option: ")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break

    if input_value == "1":
        maintenance()                 
    elif input_value == "2":
        hr()              
    elif input_value == "3":
        finance()
    elif input_value == "4":
        auditor()
    elif input_value == "5":
        safety()
    elif input_value == "6":
        project_manager()
    elif input_value == "7":
        administration()
    elif input_value == "8":
        procurement()
    elif input_value == "9":
        warehouse()  
    elif input_value == "10":
        equipment()
    elif input_value == "11":
        info_tech()
    elif input_value == "12":
        other()                       
    elif input_value == "13":
        print(f"{first_name} {last_name} has clocked out for the day.")
    else:
        print("Invalid selection. Please try again.")
        input("Press Enter to continue ...")


#other Function done
def other():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Temporary Contract |===")
        print("1.  Clock out")
        print("2.  Work Order")
        input_value = None  # Initialize input_value
        try:
            input_value = input("Select an option: ")
            if input_value == '1':
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == '2':
                loaders.count_rows_csv_WorkOrder(WORK_ORDER_FILE)
                print(f"Current WorkOrders: {loaders.count_rows_csv_WorkOrder(WORK_ORDER_FILE)}")
                loaders.add_work_order(WORK_ORDER_FILE)
            else:
                print("Invalid selection. Please try again.")
                input("Press Enter to continue ...")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    pass

#program call to start
if __name__ == "__main__":
    ecos = []
    associate_id, first_name, last_name, job_title = assoc.id_validate()
    pull_menu(associate_id, first_name, last_name, job_title)





