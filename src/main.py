#main file for selection system
import time
import os
import loaders
import sys
import associate as assoc
import reports
from datetime import datetime





#changed datetime to exclude miliseconds
original_datetime = datetime.now()
formatted_datetime = original_datetime.strftime('%m-%d-%Y \n%H:%M')


# need multi level UI for job levels 5-7, 4, 1-3


os.system('cls' if os.name == 'nt' else 'clear')

#defining the main UI 
def pull_menu(associate_id, first_name, last_name):
    
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print(f"Configuring Employee Job Type Menu for id {associate_id} ....")
        time.sleep(2)
        print(f"Taking you to {first_name} {last_name} menu")

        if associate_id >= 0 and associate_id <= 31:
            maintenance()
        elif associate_id >= 32 and associate_id <= 37:
            hr()
        elif associate_id >= 38 and associate_id <= 42:
            finance()
        elif associate_id >= 43 and associate_id <= 45:
            auditor()
        elif associate_id >= 46 and associate_id <= 52:
            safety()
        elif associate_id >= 53 and associate_id <= 56:
            project_manager()
        elif associate_id >= 57 and associate_id <= 68:
            administration()
        elif associate_id >= 69 and associate_id <= 76:
            procurement()
        elif associate_id >= 76 and associate_id <= 100:
            warehouse()
        elif associate_id >= 101 and associate_id <= 105:
            equipment()
        elif associate_id >= 106 and associate_id <= 111:
            info_tech()
        elif associate_id == 112:
            other()
        elif associate_id >= 113:
            print("\n Employee needs to seek HR. Please contact them right away.")
            time.sleep(3)
        else:
            print("\nInput cancelled or not available. Exiting program.")
            sys.exit()
def maintenance():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Maintenance |===")
        print("1.  Clock out")
        print("2.  Equipment Check In")
        print("3.  Equipment Check Out")
        try:
            input_value = input("Select an option: ")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break    
    if input_value == "1":
        print(f"{first_name} {last_name} has clocked out for the day.")
    elif input_value == "2":
        print (f"Please return your tools to the window clerk now")
    elif input_value == "3":
        print (f"Please grab your tools from the window clerk now")
    else:
        print("\nInput cancelled or not available. Exiting program.")


#HR function
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
        try:
            input_value = input("Select an option: ")
            if input_value == '1':
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == "2":
                loaders.add_employee()
            elif input_value == '3':
                loaders.remove_employee()
            elif input_value == '4':
                loaders.update_employee()
            else:
                print("\nInput cancelled or not available. Exiting program.")
    
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    

#finance function
def finance():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Finance |===")
        print("1.  Clock out")
        print("2.  Lost and Damage Equipment Report")
        print("3.  Equipment Price Checker")
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == '2':
                loaders.lost_damage()
            elif input_value == '3':
                loaders.equipment_price()
            else:
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    
#Auditor function
def auditor():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Auditor |===")
        print("1.  Clock out")
        print("2.  Generate All Reports")
        
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == '2':
                reports.auditor_report()
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
#Safety Function
def safety(): #clayton
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Safety |===")
        print("1.  Clock out")
        print("2.  Certificate Employee Update") #Certificate update for empoyee
        print("3.  Certificate Equipment Update")#Certificate update for equipment
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
#Project manager function
def project_manager():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Manager |===")
        print("1.  Clock out")
        print("2.  Generate All Reports")
        
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
    
#Administration function
def administration():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Admin |===")
        print("1.  Check out")
        print("2.  Live Status Report")
        print("3.  Email report")
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
    
#Procurement Function
def procurement(): #clatyton
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Procurement |===")
        print("1.  Check out")
        print("2.  Inventory Report")
        print("3.  Update Inventory tools/equipment")
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input_value == "2":
                reports.inventory_reports_menu()
            elif input_value == "3":
                loaders.inventory_tool()
            else:    
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    
#Warehouse function
def warehouse():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Warehouse |===")
        print("1.  Check out")
        print("2.  Materials Status Update")
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input == '2':
                loaders.material_update()
            else:
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
#Equipment Function
def equipment():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Tool Room |===")
        print("1.  Check out")
        print("2.  Equipment Status Update")
        try:
            input_value = input("Select an option: ")
            if input_value == "1":
                print(f"{first_name} {last_name} has clocked out for the day.")
            elif input == '2':
                loaders.equipment_status()
            else:
                print("\nInput cancelled or not available. Exiting program.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 




#info_tech function
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
        finance()           #
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
    else:
        print("Invalid selection. Please try again.")
        input("Press Enter to continue ...")






#other Function
def other():
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Temporary Contract |===")
        print("1.  Check out")
        print("2.  Work Order")
        try:
            input_value = input("Select an option: ")
            if input_value == '1':
                print(f"{first_name} {last_name} has clocked out for the day.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")
        break 
    pass

#program call to start
if __name__ == "__main__":
    ecos = []
    associate_id, first_name, last_name = assoc.id_validate()
    pull_menu(associate_id, first_name, last_name)




# def equipment_in(ecos)
# def equipmetn_out(ecos)
# def reports(ecos)
# def live_status(ecos)
