#main file for selection system
import datetime
import os

# need multi level UI for job levels 5-7, 4, 1-3




#defining the main UI 
def main_menu(ecos):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(datetime.datetime.now())
        print("===| ECOS |===")
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
        input_value = input("Select an option: ")

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

def maintenance():
    clock_inout(id)
    job_type = 1
    print(job_type)

def clock_inout(id): # function to valid user ID and compare VS database **Still vising validation waiting upon meeting
    os.system('cls' if os.name == 'nt' else 'clear')
    id = input("Enter your personel number: ")
    print("Validating assocaite ID")
    time.sleep(4)
    if id == associate.id :
        print("Associate entered a valid personel ID.")
        in_out = input(associate.name + "enter Y to clock in or N to clock out")
    else:
        print("Invalid personel ID")



if __name__ == "__main__":
    ecos = []
    main_menu(ecos)




# def equipment_in(ecos)
# def equipmetn_out(ecos)
# def reports(ecos)
# def live_status(ecos)
