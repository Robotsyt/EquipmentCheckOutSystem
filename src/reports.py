# ************************************needs Query search using something like a def index(): *request.method == "GET": ********************************************  Maybe
#needs predefined report options 
    #1. All equipment report //for individual print (associate_name, ID, time, equipment #)
    #2. Employee Certifications print (assocaite_name, id, employee_certification)
    #3. Material/tool location report 1st print(Material_id, material_location) 2nd print (============) *seperationg the two sections 3rd print(tool_id, tool_location)
import pandas as pd
import os
import time

# File paths
EMPLOYEE_FILE = "EquipmentCheckOutSystem-main/database/Employee.csv"
EQUIPMENT_FILE = "EquipmentCheckOutSystem-main/database/Equipment.csv"
EMPLOYEE_CERT_FILE = "EquipmentCheckOutSystem-main/database/Employee_Certification.csv"
MATERIAL_LOC_FILE = "EquipmentCheckOutSystem-main/database/MaterialLocation.csv"
TOOL_LOC_FILE = "EquipmentCheckOutSystem-main/database/ToolRoomTools.csv"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def paginate(df, page_size=10):
    total_pages = (len(df) + page_size - 1) // page_size
    current_page = 0

    while True:
        clear()
        start = current_page * page_size
        end = start + page_size
        print(df.iloc[start:end].to_string(index=False))
        print(f"\nPage {current_page + 1} of {total_pages}")
        action = input("N = Next, P = Previous, Q = Quit: ").strip().lower()

        if action == 'n' and current_page < total_pages - 1:
            current_page += 1
        elif action == 'p' and current_page > 0:
            current_page -= 1
        elif action == 'q':
            break
        else:
            print("Invalid input. Try again.")
            time.sleep(1)

def equipment_report():
    df = pd.read_csv(EQUIPMENT_FILE)
    df.columns = ["Equipment Number", "Equipment Type"]
    paginate(df)

def employee_certifications():
    emp_df = pd.read_csv(EMPLOYEE_FILE)
    cert_df = pd.read_csv(EMPLOYEE_CERT_FILE)
    merged = pd.merge(cert_df, emp_df, left_on='EmployeeID', right_on='EmployeeID')
    merged = merged[["EmployeeID", "F_Name", "L_Name", "CertificationID"]]
    merged.columns = ["Employee ID", "First Name", "Last Name", "Certification ID"]
    paginate(merged)

def material_tool_locations():
    mat_df = pd.read_csv(MATERIAL_LOC_FILE)
    tool_df = pd.read_csv(TOOL_LOC_FILE)

    # Adjust columns to match actual CSV headers
    mat_df = mat_df[["MaterialID", "WarhouseID"]]
    mat_df.columns = ["Material ID", "Material Location"]

    tool_df.columns = tool_df.columns.str.strip()  # Remove any extra spaces
    tool_df = tool_df[["ToolID", "Tool Specifics"]]
    tool_df.columns = ["Tool ID", "Tool Description"]



    print("=== Material Location Report ===")
    paginate(mat_df)

    print("=== Tool Location Report ===")
    paginate(tool_df)




def reports_menu():
    while True:
        clear()
        print("===| Reports Menu |===")
        print("1. All Equipment Report")
        print("2. Employee Certifications")
        print("3. Material/Tool Location Report")
        print("4. Exit")
        choice = input("Enter your selection: ").strip()

        if choice == '1':
            equipment_report()
        elif choice == '2':
            employee_certifications()
        elif choice == '3':
            material_tool_locations()
        elif choice == '4':
            break
        else:
            print("Invalid selection.")
            pause()
