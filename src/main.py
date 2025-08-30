# Main file for the Equipment Check Out System (ECOS)
# Imports standard and custom modules for system functionality
import time  # For sleep/delays
import os  # For clearing the terminal
import loaders  # Custom module for loading and updating data
import sys  # For exiting the program
import associate as assoc  # Custom module for associate/employee logic
import reports  # Custom module for generating reports
from datetime import datetime  # For date and time formatting

# File path constants for all required CSV files
CLOCK_FILE = "database/Clock.csv"
EMPLOYEE_FILE = "database/Employee.csv"
JOB_INFO_FILE = "database/JobInfo.csv"
EQUIPMENT_FILE = "database/Equipment.csv"
EMPLOYEE_CERT_FILE = "database/EmployeeCertification.csv"
LOCATION_FILE = "database/LocationsList.csv"
MATERIAL_LOC_FILE = "database/MaterialInventory.csv"
TRANSACTIONS_FILE = 'database/Transactions.csv'
WORK_ORDER_FILE = 'database/WorkOrder.csv'

# Format the current date and time for display (no milliseconds)
original_datetime = datetime.now()
formatted_datetime = original_datetime.strftime('%m-%d-%Y \n%H:%M')

# Clear the terminal screen at program start
os.system('cls' if os.name == 'nt' else 'clear')

# Main menu router: directs user to the correct menu based on job title
def pull_menu(associate_id, first_name, last_name, job_title):
    # Wait for 2 seconds for user experience
    time.sleep(2)
    # Clear the screen for a clean menu
    os.system('cls' if os.name == 'nt' else 'clear')
    # Show the current date/time
    print(formatted_datetime)
    # Show which menu is being configured
    print(f"Configuring Employee Job Type Menu for id {associate_id} ....")
    time.sleep(2)
    # Greet the user
    print(f"Taking you to {first_name} {last_name} menu")

    # Route to the correct menu based on job_title code
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
# Maintenance menu: handles all maintenance-related actions for the user
def maintenance():
    while True:
        # Wait for 1 second for user experience
        time.sleep(1)
        # Clear the screen for a clean menu
        os.system('cls' if os.name == 'nt' else 'clear')
        # Show the current date/time
        print(formatted_datetime)
        # Print the maintenance menu options
        print("===| Maintenance |===")
        print("1.  Clock out")
        print("2.  Equipment Check In")
        print("3.  Equipment Check Out")
        print("4.  Employee Personal Equipment Inventory")
        print("5.  return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None
        try:
            # Prompt user for menu selection
            input_value = input("Select an option: ")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break    
    # Handle user selection
    if input_value == "1":
        # User clocks out
        print(f"{first_name} {last_name} has clocked out for the day.")
    elif input_value == "2":
        # Equipment check in process
        loaders.count_rows_trans(TRANSACTIONS_FILE)
        loaders.transactions(TRANSACTIONS_FILE)
        loaders.tool_location_update(EQUIPMENT_FILE)
        print (f"Please return your tools to the window clerk now")
    elif input_value == "3":
        # Equipment check out process
        print ("Select the tool room you are checking out from.")
        loaders.inventory_tool_room(EQUIPMENT_FILE)
        print ("The list generated is the tools available for check out.")
        loaders.count_rows_trans(TRANSACTIONS_FILE)
        loaders.transactions(TRANSACTIONS_FILE)
        loaders.tool_location_update(EQUIPMENT_FILE)
        print (f"Please grab your tools from the window clerk now")
    elif input_value == "4":
        # Show employee's personal equipment inventory
        loaders.inventory_employee_tool(EQUIPMENT_FILE)
    elif input_value == "5":
        # Restart the program
        os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        print("\nInput cancelled or not available. Exiting program.")


# HR menu: handles all HR-related actions for the user
def hr():
    while True:
        # Wait for 1 second for user experience
        time.sleep(1)
        # Clear the screen for a clean menu
        os.system('cls' if os.name == 'nt' else 'clear')
        # Show the current date/time
        print(formatted_datetime)
        # Print the HR menu options
        print("===| HR |===")
        print("1.  Clock Out")
        print("2.  Add Employee")
        print("3.  Remove Employee")
        print("4.  Update Employee information")
        print("5.  return to start of program")
        input_value = None  # Initialize input_value
        try:
            # Prompt user for menu selection
            input_value = input("Select an option: ")
            if input_value == '1':
                # User clocks out
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == "2":
                # Add a new employee
                loaders.count_rows_csv(EMPLOYEE_FILE)
                print(f"Total employees: {loaders.count_rows_csv(EMPLOYEE_FILE)}")
                loaders.add_employee(EMPLOYEE_FILE)
            elif input_value == '3':
                # Remove an employee
                loaders.remove_employee(EMPLOYEE_FILE)
            elif input_value == '4':
                # Update employee information
                print("Enter 0 to skip any field, unless otherwise noted.\n")
                loaders.update_employee()
            elif input_value == "5":
                 # Restart the program
                os.execv(sys.executable, [sys.executable] + sys.argv)   
            else:
                print("\nInput cancelled or not available. Exiting program.")
    
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    

#finance function done
def finance():
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(formatted_datetime)  # Display the current date and time
        print("===| Finance |===")  # Print the Finance menu header
        print("1.  Clock out")  # Option 1: Clock out
        print("2.  Lost and Damage Equipment Report")  # Option 2: Lost and Damage Equipment Report
        print("3.  Equipment Price Checker")  # Option 3: Equipment Price Checker
        print("4.  return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None
        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")  # Handle clock out
            elif input_value == '2':
                loaders.inventory_condition_tool(EQUIPMENT_FILE)  # Call function for lost/damage report
            elif input_value == '3':
                loaders.individual_equipment_price(EQUIPMENT_FILE)  # Call function for equipment price check
            elif input_value == "4":
                 # Restart the program
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                print("\nInput cancelled or not available. Exiting program.")  # Handle invalid input
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration
    
#Auditor function done
def auditor():
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(formatted_datetime)  # Display the current date and time
        print("===| Auditor |===")  # Print the Auditor menu header
        print("1.  Clock out")  # Option 1: Clock out
        print("2.  Generate All Reports")  # Option 2: Generate all reports
        print("3.  return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None
        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")  # Handle clock out
            elif input_value == '2':
                reports.auditor_report()  # Call function to generate auditor report
            elif input_value == "3":
                 # Restart the program
                os.execv(sys.executable, [sys.executable] + sys.argv)
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration
#Safety Function  pending functions 2 and 3
def safety(): #clayton
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(formatted_datetime)  # Display the current date and time
        print("===| Safety |===")  # Print the Safety menu header
        print("1.  Clock out")  # Option 1: Clock out
        print("2.  Certificate Employee Update")  # Option 2: Certificate update for employee
        print("3.  Certificate Equipment Update")  # Option 3: Certificate update for equipment
        print("4.  return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None
        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")  # Handle clock out
            elif input_value == '2':
                loaders.certificate_employee()  # Call function to update employee certificate
            elif input_value == '3':
                loaders.certificate_equipment()  # Call function to update equipment certificate
            elif input_value == "4":
                 # Restart the program
                os.execv(sys.executable, [sys.executable] + sys.argv)    
            else: 
                print("\nInput cancelled or not available. Exiting program.")  # Handle invalid input
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration
    pass
#Project manager function done
def project_manager():
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(formatted_datetime)  # Display the current date and time
        print("===| Manager |===")  # Print the Manager menu header
        print("1.  Clock out")  # Option 1: Clock out
        print("2.  Generate All Reports")  # Option 2: Generate all reports
        print("3.  return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None
        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")  # Handle clock out
            elif input_value == '2':
                reports.reports_menu()  # Call function to generate all reports
            elif input_value == "3":
                 # Restart the program
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                print("\nInput cancelled or not available. Exiting program.")  # Handle invalid input
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration
    
#Administration function  pending function 3
def administration():
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(formatted_datetime)  # Display the current date and time
        print("===| Admin |===")  # Print the Admin menu header
        print("1.  Clock out")  # Option 1: Clock out
        print("2.  Live Status Report")  # Option 2: Live status report
        print("3.  Email report")  # Option 3: Email report
        print("4.  return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None
        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")  # Handle clock out
            elif input_value == "2":
                reports.live_reports()  # Call function for live status report
            elif input_value == "3":
                reports.email_report()  # Call function for email report
            elif input_value == "4":
                 # Restart the program
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else: 
                print("\nInput cancelled or not available. Exiting program.")  # Handle invalid input
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration
    
#Procurement Function done
def procurement():
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(formatted_datetime)  # Display the current date and time
        print("===| Procurement |===")  # Print the Procurement menu header
        print("1.  Clock out")  # Option 1: Clock out
        print("2.  Inventory Report")  # Option 2: Inventory report
        print("3.  Update Inventory tools/equipment")  # Option 3: Update inventory tools/equipment
        print("4.  return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None
        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")  # Handle clock out
            elif input_value == "2":
                loaders.inventory_tool_room(EQUIPMENT_FILE)  # Call function for inventory report
            elif input_value == "3":
                print("Enter 0 to skip any field, unless otherwise noted.\n")  # Prompt for skipping fields
                loaders.update_inventory_tool(EQUIPMENT_FILE)  # Call function to update inventory
            elif input_value == "4":
                 # Restart the program
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:    
                print("\nInput cancelled or not available. Exiting program.")  # Handle invalid input
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration
    
#Warehouse function done
def warehouse():
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(formatted_datetime)  # Display the current date and time
        print("===| Warehouse |===")  # Print the Warehouse menu header
        print("1.  Clock out")  # Option 1: Clock out
        print("2.  Materials Update")  # Option 2: Materials update
        print("3.  Inventory Report")  # Option 3: Inventory report
        print("4.  return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None
        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")  # Handle clock out
            elif input == '2':
                print("Enter 0 to skip any field, unless otherwise noted.\n")  # Prompt for skipping fields
                loaders.material_update()  # Call function to update materials
            elif input == '3':
                loaders.inventory_materials(MATERIAL_LOC_FILE)  # Call function for inventory report
            elif input_value == "4":
                 # Restart the program
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                print("\nInput cancelled or not available. Exiting program.")  # Handle invalid input
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration


#Equipment Function done
def equipment():
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(formatted_datetime)  # Display the current date and time
        print("===| Tool Room |===")  # Print the Tool Room menu header
        print("1.  Clock out")  # Option 1: Clock out
        print("2.  Equipment Location Update")  # Option 2: Equipment location update
        print("3.  Equipment Inventory")  # Option 3: Equipment inventory
        print("4.  Update Equipment Condition")  # Option 4: Update equipment condition
        print("5.  Equipment Status")  # Option 5: Equipment status
        print("6.  return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None
        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")  # Handle clock out
            elif input == '2':
                loaders.tool_location_update(EQUIPMENT_FILE)  # Call function to update equipment location
            elif input == '3':
                loaders.inventory_tool_room(EQUIPMENT_FILE)  # Call function for equipment inventory
            elif input == '4':
                loaders.tool_condition_update(EQUIPMENT_FILE)  # Call function to update equipment condition
            elif input == '5':
                loaders.equipment_status(EQUIPMENT_FILE='database/Equipment.csv')  # Call function for equipment status
            elif input_value == "6":
                 # Restart the program
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                print("\nInput cancelled or not available. Exiting program.")  # Handle invalid input
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration




#info_tech function done
def info_tech():
    while True:
        time.sleep(3)  # Pause for 3 seconds for user experience
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(formatted_datetime)  # Display the current date and time
        print("===| IT |===")  # Print the IT menu header
        print("1.  Clock Out")  # Option 1: Maintenance
        print("2.  Maintenance")  # Option 1: Maintenance
        print("3.  HR")  # Option 2: HR
        print("4.  Finance")  # Option 3: Finance
        print("5.  Auditor/Compliance")  # Option 4: Auditor/Compliance
        print("6.  Safety")  # Option 5: Safety
        print("7.  Project Manager")  # Option 6: Project Manager
        print("8.  Administration")  # Option 7: Administration
        print("9.  Procurement")  # Option 8: Procurement
        print("10.  Warehouse")  # Option 9: Warehouse
        print("11. Equipment")  # Option 10: Equipment
        print("12. IT")  # Option 11: IT
        print("13. Other")  # Option 12: Other
        print("14. return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None

        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration

    # Route to the correct function based on user selection
    if input_value == "1":
        print(f"{first_name} {last_name} has clocked out for the day.")  # Handle clock out
    elif input_value == "2":
        maintenance()                 # Call maintenance menu
    elif input_value == "3":
        hr()              # Call HR menu
    elif input_value == "4":
        finance()         # Call finance menu
    elif input_value == "5":
        auditor()         # Call auditor menu
    elif input_value == "6":
        safety()          # Call safety menu
    elif input_value == "7":
        project_manager() # Call project manager menu
    elif input_value == "8":
        administration()  # Call administration menu
    elif input_value == "9":
        procurement()     # Call procurement menu
    elif input_value == "10":
        warehouse()       # Call warehouse menu
    elif input_value == "11":
        equipment()       # Call equipment menu
    elif input_value == "12":
        info_tech()       # Call IT menu again
    elif input_value == "13":
        other()           # Call other menu
    elif input_value == "14":
         # Restart the program
        os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        print("Invalid selection. Please try again.")  # Handle invalid input
        input("Press Enter to continue ...")  # Wait for user to acknowledge


#other Function done
def other():
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(formatted_datetime)  # Display the current date and time
        print("===| Temporary Contract |===")  # Print the Temporary Contract menu header
        print("1.  Clock out")  # Option 1: Clock out
        print("2.  Work Order")  # Option 2: Work order
        print("3.  return to start of program")# Option : restart entire program
        input_value = None  # Initialize input_value to None
        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == '1':
                print(f"{first_name} {last_name} has clocked out for the day.")  # Handle clock out
            elif input_value == '2':
                loaders.count_rows_csv_WorkOrder(WORK_ORDER_FILE)  # Count current work orders
                print(f"Current WorkOrders: {loaders.count_rows_csv_WorkOrder(WORK_ORDER_FILE)}")  # Display current work orders
                loaders.add_work_order(WORK_ORDER_FILE)  # Call function to add work order
            elif input_value == "4":
                # Restart the program
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                print("Invalid selection. Please try again.")  # Handle invalid input
                input("Press Enter to continue ...")  # Wait for user to acknowledge
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration
    pass

#program call to start
if __name__ == "__main__":
    associate_id, first_name, last_name, job_title = assoc.id_validate()
    pull_menu(associate_id, first_name, last_name, job_title)
    


