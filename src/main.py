#main file for selection system
import time
import os
import associate as assoc
from datetime import datetime




#changed datetime to exclude miliseconds
original_datetime = datetime.now()
formatted_datetime = original_datetime.strftime('%m-%d-%Y \n%H:%M')


# need multi level UI for job levels 5-7, 4, 1-3


os.system('cls' if os.name == 'nt' else 'clear')

#defining the main UI 
def main_menu(associate_id, first_name, last_name):
    while True:
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(formatted_datetime)
        print("===| Job Level Menu |===")
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
        maintenance(associate_id, first_name, last_name)                 
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

def maintenance(associate_id, first_name, last_name):
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
    # add employee
    # remove employee
    # 
    #
    pass

#finance function
def finance():
    pass
#Auditor function
def auditor():
    pass
#Safety Function
def safety():
    pass
#Project manager function
def project_manager():
    pass
#Administration function
def administration():
    # live status of checked out equipment 
    # email print out 
    pass
#Procurement Function
def procurement():
    pass
#Warehouse function
def warehouse():
    pass
#Equipment Function
def equipment():
    pass
#info_tech function
def info_tech():
    # All menu functions
    pass
#other Function
def other():
    #other employees as clock in or clock out
    pass

#program call to start
if __name__ == "__main__":
    ecos = []
    associate_id, first_name, last_name = assoc.id_validate()
    main_menu(associate_id, first_name, last_name)




# def equipment_in(ecos)
# def equipmetn_out(ecos)
# def reports(ecos)
# def live_status(ecos)
