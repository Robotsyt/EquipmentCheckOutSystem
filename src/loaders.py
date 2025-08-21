import csv
import pandas as pd
# File paths
EMPLOYEE_FILE = "database/Employee.csv"
EQUIPMENT_FILE = "database/Equipment.csv"
EMPLOYEE_CERT_FILE = "database/Employee_Certification.csv"
MATERIAL_LOC_FILE = "database/MaterialLocation.csv"
TOOL_LOC_FILE = 'database/ToolRoomTools.csv'
#hr functions antonio
def paginate(df, page_size=10):
    total_pages = (len(df) + page_size - 1) // page_size
    current_page = 0
def add_employee():

    with open ('database/Employee.csv', 'w'):       #opens the filepath to whatever csv file
        my_list = []
        identify_data = csv.reader()
        next(identify_data) #skips the header information

        for row in identify_data:
            my_list.append(row)
        return my_list
    pass
def remove_employee():
    pass
def update_employee():
    pass


#finance jon
def lost_damage():
    pass
def equipment_price():
    pass

#safety Clayton
def certificate_employee():
    emp_df = pd.read_csv(EMPLOYEE_FILE)
    cert_df = pd.read_csv(EMPLOYEE_CERT_FILE)
    merged = pd.merge(cert_df, emp_df, left_on='EmployeeID', right_on='EmployeeID')
    merged = merged[["EmployeeID", "F_Name", "L_Name", "CertificationID"]]
    merged.columns = ["Employee ID", "First Name", "Last Name", "Certification ID"]
    paginate(merged)

def certificiate_equipment():
    pass

#procurement functions Clayton
def inventory_tool():
    pass

#Warehouse functions ANYONE
def material_update():
    pass

#Equipment functions Brandon
def equipment_status():
    pass