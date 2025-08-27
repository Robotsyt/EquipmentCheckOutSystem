import csv
import pandas as pd
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
# maintenance functions
def equipment_in():
    pass
def equipment_out():
    pass

def inventory_employee_tool(EQUIPMENT_FILE):
    EQUIPMENT_FILE = 'database/Equipment.csv'  # input file path and desired output file path
    columns_to_keep = ['Item #', 'Item Info', 'ToolBoxJobID', 'EmployeeID']
    employee = input("Enter Employee ID: ") # 
    try:
        # Read the CSV file into a DataFrame
        with open(EQUIPMENT_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(infile, encoding='utf-8')

        # Check if the specified column exists
        missing_columns = [col for col in columns_to_keep if col not in df.columns]
        if missing_columns:
            print(f"Error: The following columns are missing in the CSV file: {missing_columns}")
            return
        # Select only the desired columns
        df = df[columns_to_keep]

        if 'Item #' not in df.columns:
            print("Error: 'Item #' column not found in the CSV file.")
            return

        # Filter rows where the column matches the given value
        filtered_df = df[df['EmployeeID'] == employee]

        # Check if any rows match the item
        if filtered_df.empty:
            print(f"No rows found with '{'EmployeeID'}' equal to '{employee}'.")
        else:
            print("Filtered rows:")
            print(filtered_df)

    except FileNotFoundError:
        print(f"Error: File '{EQUIPMENT_FILE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


#hr functions antonio
def paginate(df, page_size=10):
    total_pages = (len(df) + page_size - 1) // page_size
    current_page = 0
# count employees
def count_rows_csv(EMPLOYEE_FILE): # this shows before main file function
    try:
        with open('database/Employee.csv', mode='r') as file:
            reader = csv.reader(file)
            row_count = sum(1 for row in reader)  # Count rows
        return row_count - 1  # Subtract 1 if the first row is a header
    except FileNotFoundError:
        print(f"Error: File '{EMPLOYEE_FILE}' not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# add employee
def add_employee(EMPLOYEE_FILE):
    # New row to append (list of values)
    employID = count_rows_csv(EMPLOYEE_FILE)+1  #this counts the employees and adds 1
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    hiredate = input("Enter Hire Date as YYYY-MM-DD: ")
    jobtitle = input("Enter Job Title ID 1-112: ")
    phone = input("Enter Phone Number as (###)###-####: ")
    email = input("Enter Email Address: ")
    manager = input("Enter Manager ID: ")
    #    Appends a new row to an existing CSV file.
    new_employee_row = [employID, fname, lname, hiredate, jobtitle, phone, email, manager]

    try:
        # Open the file in append mode ('a') and set newline='' to avoid extra blank lines
        with open('database/Employee.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_employee_row)  # Append the new row
        print(f"Row {new_employee_row} successfully added to {EMPLOYEE_FILE}.")
    except Exception as e:
        print(f"Error: {e}")

# remove employee
def remove_employee(EMPLOYEE_FILE): #this function removes employees by EmployeeID
    EMPLOYEE_FILE = 'database/Employee.csv'  # input file path and desired output file path
    removeemployeeID = int(input("Enter Employee ID to remove: ")) # value to remove
    try:
            # Open the file for reading
        with open(EMPLOYEE_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(EMPLOYEE_FILE)

            # Remove rows where 'EmployeeID' column equals provided value
            df_filtered = df[df['EmployeeID'] != removeemployeeID]
            # Save the DataFrame to CSV file
            df_filtered.to_csv(EMPLOYEE_FILE, index=False)

        print(f"Employee number '{removeemployeeID}' has been removed.")
    except FileNotFoundError:
        print(f"Error: The file '{EMPLOYEE_FILE}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# update employee
def update_employee():
    EMPLOYEE_FILE = 'database/Employee.csv'  # input file path and desired output file path
    employeeID = int(input("Enter Employee ID to update: ")) # employeeID to update
    try:
            # Open the file for reading
        with open(EMPLOYEE_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(EMPLOYEE_FILE)

            # Select rows where 'EmployeeID' column equals provided value
            df_filtered = df[df['EmployeeID'] == employeeID]
            # Update the row with new values
            df_filtered['F_Name'] = input("Enter First Name: ")
            if df_filtered['F_Name'] == '0':
                df_filtered['F_Name'] = df_filtered['F_Name']
            else:
                df_filtered['F_Name'] = input("Enter First Name: ")
            df_filtered['L_Name'] = input("Enter Last Name: ")
            if df_filtered['L_Name'] == '0':
                df_filtered['L_Name'] = df_filtered['L_Name']
            else:
                df_filtered['L_Name'] = input("Enter Last Name: ")
            df_filtered['HireDate'] = input("Enter Hire Date as YYYY-MM-DD: ")
            if df_filtered['HireDate'] == '0':
                df_filtered['HireDate'] = df_filtered['HireDate']
            else:
                df_filtered['HireDate'] = input("Enter Hire Date as YYYY-MM-DD: ")
            df_filtered['JobTitleID'] = input("Enter Job Title ID 1-112: ")
            if df_filtered['JobTitleID'] == '0':
                df_filtered['JobTitleID'] = df_filtered['JobTitleID']
            else:
                df_filtered['JobTitleID'] = input("Enter Job Title ID 1-112: ")
            df_filtered['Phone'] = input("Enter Phone Number as (###)###-####: ")
            if df_filtered['Phone'] == '0':
                df_filtered['Phone'] = df_filtered['Phone']
            else:
                df_filtered['Phone'] = input("Enter Phone Number as (###)###-####: ")
            df_filtered['Email'] = input("Enter Email Address: ")
            if df_filtered['Email'] == '0':
                df_filtered['Email'] = df_filtered['Email']
            else:
                df_filtered['Email'] = input("Enter Email Address: ")
            df_filtered['ManagerID'] = input("Enter Manager ID: ")
            if df_filtered['ManagerID'] == '0':
                df_filtered['ManagerID'] = df_filtered['ManagerID']
            else:
                df_filtered['ManagerID'] = input("Enter Manager ID: ")
            # Save the DataFrame to CSV file
            df_filtered.to_csv(EMPLOYEE_FILE, index=False)

        print(f"Employee number '{employeeID}' has been updated.")
    except FileNotFoundError:
        print(f"Error: The file '{EMPLOYEE_FILE}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# finance functions
# lost_damage inventory
def inventory_condition_tool(EQUIPMENT_FILE):
    EQUIPMENT_FILE = 'database/Equipment.csv'  # input file path and desired output file path
    columns_to_keep = ['Item #', 'Item Info', 'ToolRoomName', 'ToolRoomID', 'Condition', 'Price']
    condition = input("Enter Condition to find Good, Damaged, Lost: ") # condition to find
    try:
        # Read the CSV file into a DataFrame
        with open(EQUIPMENT_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(infile, encoding='utf-8')

        # Check if the specified column exists
        missing_columns = [col for col in columns_to_keep if col not in df.columns]
        if missing_columns:
            print(f"Error: The following columns are missing in the CSV file: {missing_columns}")
            return
        # Select only the desired columns
        df = df[columns_to_keep]

        if 'Condition' not in df.columns:
            print("Error: 'Condition' column not found in the CSV file.")
            return
        
        # Filter rows where the column matches the given value
        filtered_df = df[df['Condition'] == condition]

        # Check if any rows match the condition
        if filtered_df.empty:
            print(f"No rows found with '{'Condition'}' equal to '{condition}'.")
        else:
            print("Filtered rows:")
            print(filtered_df)

    except FileNotFoundError:
        print(f"Error: File '{EQUIPMENT_FILE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# price per item
def individual_equipment_price(EQUIPMENT_FILE):
    EQUIPMENT_FILE = 'database/Equipment.csv'  # input file path and desired output file path
    columns_to_keep = ['Item #', 'Item Info', 'Condition', 'Price']
    item = input("Enter Item Number: ") # 
    try:
        # Read the CSV file into a DataFrame
        with open(EQUIPMENT_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(infile, encoding='utf-8')

        # Check if the specified column exists
        missing_columns = [col for col in columns_to_keep if col not in df.columns]
        if missing_columns:
            print(f"Error: The following columns are missing in the CSV file: {missing_columns}")
            return
        # Select only the desired columns
        df = df[columns_to_keep]

        if 'Item #' not in df.columns:
            print("Error: 'Item #' column not found in the CSV file.")
            return

        # Filter rows where the column matches the given value
        filtered_df = df[df['Item #'] == item]

        # Check if any rows match the item
        if filtered_df.empty:
            print(f"No rows found with '{'Item #'}' equal to '{item}'.")
        else:
            print("Filtered rows:")
            print(filtered_df)

    except FileNotFoundError:
        print(f"Error: File '{EQUIPMENT_FILE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#auditor functions
def auditor_report():  # see reports.py file
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

#project manager functions   working on this
def reports_menu():  # see reports.py file
    pass

# administration functions
def live_reports(): # see reports.py file
    pass

#procurement functions Clayton
  # see inventory_tool_room function in equipment functions section
def update_inventory_tool(EQUIPMENT_FILE):
    EQUIPMENT_FILE = 'database/Equipment.csv'  # input file path and desired output file path
    item = input("Enter Item Number: ")
    try:
        # Open the file for reading
        with open(EQUIPMENT_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(EQUIPMENT_FILE)
            # Select rows where 'Item #' column equals provided value
            df_filtered = df[df['Item #'] == item]
            # Update the row with new values
            df_filtered['Equipment #'] = input("Enter Equipment #: ")
            if df_filtered['Equipment #'] == '0':
                df_filtered['Equipment #'] = df_filtered['Equipment #']
            else:
                df_filtered['Equipment #'] = input("Enter Equipment #: ")
                
            df_filtered['Equipment Type'] = input("Enter Equipment Type: ")
            if df_filtered['Equipment Type'] == '0':
                df_filtered['Equipment Type'] = df_filtered['Equipment Type']
            else:
                df_filtered['Equipment Type'] = input("Enter Equipment Type: ")
                
            df_filtered['Tool #'] = input("Enter Tool #: ")
            if df_filtered['Tool #'] == '0':
                df_filtered['Tool #'] = df_filtered['Tool #']
            else:
                df_filtered['Tool #'] = input("Enter Tool #: ")
                
            df_filtered['EquipToolID'] = input("Enter EquipToolID: ")
            if df_filtered['EquipToolID'] == '0':
                df_filtered['EquipToolID'] = df_filtered['EquipToolID']
            else:
                df_filtered['EquipToolID'] = input("Enter EquipToolID: ")
                
            df_filtered['Tool Specifics'] = input("Enter Tool Specifics: ")
            if df_filtered['Tool Specifics'] == '0':
                df_filtered['Tool Specifics'] = df_filtered['Tool Specifics']
            else:
                df_filtered['Tool Specifics'] = input("Enter Tool Specifics: ")
                
            df_filtered['Item #'] = input("Enter Item #: ")
            if df_filtered['Item #'] == '0':
                df_filtered['Item #'] = df_filtered['Item #']
            else:
                df_filtered['Item #'] = input("Enter Item #: ")
                
            df_filtered['EquipToolItemID'] = input("Enter EquipToolItemID: ")
            if df_filtered['EquipToolItemID'] == '0':
                df_filtered['EquipToolItemID'] = df_filtered['EquipToolItemID']
            else:
                df_filtered['EquipToolItemID'] = input("Enter EquipToolItemID: ")
                
            df_filtered['Item Info'] = input("Enter Item Info: ")
            if df_filtered['Item Info'] == '0':
                df_filtered['Item Info'] = df_filtered['Item Info']
            else:
                df_filtered['Item Info'] = input("Enter Item Info: ")
                
            df_filtered['ToolBox Type'] = input("Enter ToolBox Type: ")
            if df_filtered['ToolBox Type'] == '0':
                df_filtered['ToolBox Type'] = df_filtered['ToolBox Type']
            else:
                df_filtered['ToolBox Type'] = input("Enter ToolBox Type: ")
                
            df_filtered['JobID'] = input("Enter JobID: ")
            if df_filtered['JobID'] == '0':
                df_filtered['JobID'] = df_filtered['JobID']
            else:
                df_filtered['JobID'] = input("Enter JobID: ")
                
            df_filtered['ToolBoxID'] = input("Enter ToolBoxID: ")
            if df_filtered['ToolBoxID'] == '0':
                df_filtered['ToolBoxID'] = df_filtered['ToolBoxID']
            else:
                df_filtered['ToolBoxID'] = input("Enter ToolBoxID: ")
                
            df_filtered['ToolBoxJobID'] = input("Enter ToolBoxJobID: ")
            if df_filtered['ToolBoxJobID'] == '0':
                df_filtered['ToolBoxJobID'] = df_filtered['ToolBoxJobID']
            else:
                df_filtered['ToolBoxJobID'] = input("Enter ToolBoxJobID: ")
                
            df_filtered['ToolRoomName'] = input("Enter Tool Room Name: ")
            if df_filtered['ToolRoomName'] == '0':
                df_filtered['ToolRoomName'] = df_filtered['ToolRoomName']
            else:
                df_filtered['ToolRoomName'] = input("Enter Tool Room Name: ")
                
            df_filtered['EmployeeID'] = input("Enter EmployeeID: ")
            if df_filtered['EmployeeID'] == '0':
                df_filtered['EmployeeID'] = df_filtered['EmployeeID']
            else:
                df_filtered['EmployeeID'] = input("Enter EmployeeID: ")
                
            df_filtered['ToolRoomID'] = input("Enter Tool Room ID: ")
            if df_filtered['ToolRoomID'] == '0':
                df_filtered['ToolRoomID'] = df_filtered['ToolRoomID']
            else:
                df_filtered['ToolRoomID'] = input("Enter Tool Room ID: ")  
                
            df_filtered['Condition'] = input("Enter Condition: ")
            if df_filtered['Condition'] == '0':
                df_filtered['Condition'] = df_filtered['Condition']
            else:
                df_filtered['Condition'] = input("Enter Condition: ")
                
            df_filtered['CertificationID'] = input("Enter CertificationID enter N to skip: ")
            if df_filtered['CertificationID'] == 'N':
                df_filtered['CertificationID'] = df_filtered['CertificationID']
            else:
                df_filtered['CertificationID'] = input("Enter CertificationID enter N to skip: ")
            df_filtered['CertificationID2'] = input("Enter second CertificationID enter N to skip: ")
            if df_filtered['CertificationID2'] == 'N':
                df_filtered['CertificationID2'] = df_filtered['CertificationID2']
            else:
                df_filtered['CertificationID2'] = input("Enter second CertificationID enter N to skip: ")
            df_filtered['Price'] = input("Enter Price: ")
            if df_filtered['Price'] == '0':
                df_filtered['Price'] = df_filtered['Price']
            else:
                df_filtered['Price'] = input("Enter Price: ")
            # Save the DataFrame to CSV file
            df_filtered.to_csv(EQUIPMENT_FILE, index=False)
        print(f"Item number '{item}' has been updated.")
    except FileNotFoundError:
        print(f"Error: The file '{MATERIAL_LOC_FILE}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#Warehouse functions
def material_update():
    MATERIAL_LOC_FILE = 'database/MaterialInventory.csv'  # input file path and desired output file path
    materialID = int(input("Enter Material ID to update: ")) # employeeID to update
    try:
            # Open the file for reading
        with open(MATERIAL_LOC_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(MATERIAL_LOC_FILE)

            # Select rows where 'LocationID' column equals provided value
            df_filtered = df[df['MaterialID'] == materialID]
            # Update the row with new values
            df_filtered['LocationID'] = input("Enter LocationID: ")
            if df_filtered['LocationID'] == '0':
                df_filtered['LocationID'] = df_filtered['LocationID']
            else:
                df_filtered['LocationID'] = input("Enter LocationID: ")
            df_filtered['LocationID'] = input("Enter LocationID: ")
            if df_filtered['LocationName'] == '0':
                df_filtered['LocationName'] = df_filtered['Location Name']
            else:
                df_filtered['LocationName'] = input("Enter Location Name: ")
            df_filtered['JobID'] = input("Enter JobID: ")
            if df_filtered['JobID'] == '0':
                df_filtered['JobID'] = df_filtered['JobID']
            else:
                df_filtered['JobID'] = input("Enter JobID: ")
            df_filtered['MaterialName'] = input("Enter Material Name: ")
            if df_filtered['MaterialName'] == '0':
                df_filtered['MaterialName'] = df_filtered['MaterialName']
            else:
                df_filtered['MaterialName'] = input("Enter Material Name: ")
            df_filtered['Quantity'] = input("Enter New Quantity Press N to Skip: ")
            if df_filtered['Quantity'] == 'N':
                df_filtered['Quantity'] = df_filtered['Quantity']
            else:
                df_filtered['Quantity'] = input("Enter New Quantity Press N to Skip: ")
            # Save the DataFrame to CSV file
            df_filtered.to_csv(MATERIAL_LOC_FILE, index=False)

            print(f"Material number '{materialID}' has been updated.")
    except FileNotFoundError:
        print(f"Error: The file '{MATERIAL_LOC_FILE}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def inventory_materials(MATERIAL_LOC_FILE)  
    MATERIAL_LOC_FILE = 'database/MaterialInventory.csv'  # input file path and desired output file path
    location = int(input("Enter Location ID to view: ")) # employeeID to update
    try:
        # Open the file for reading
        with open(MATERIAL_LOC_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(MATERIAL_LOC_FILE)

    # Check if the specified column exists
        missing_columns = [col for col in columns_to_keep if col not in df.columns]
        if missing_columns:
            print(f"Error: The following columns are missing in the CSV file: {missing_columns}")
            return
# Select only the desired columns
        df = df[columns_to_keep]

        # Validate inputs
        df_filtered = df[df['LocationID'] == location]

    # Check if any rows match the item
        if filtered_df.empty:
            print(f"No rows found with '{'LocationID'}' equal to '{location}'.")
        else:
            print("Filtered rows:")
            print(filtered_df)
    except FileNotFoundError:
        print(f"Error: The file '{MATERIAL_LOC_FILE}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



#Equipment functions Brandon
def equipment_status(): #see inventory_condition_tool function or Claytons File
    pass
def tool_condition_update(EQUIPMENT_FILE):
    EQUIPMENT_FILE = 'database/Equipment.csv'
    item = input("Enter Item Number: ")
    condition = input("Enter New Condition: ")
    try:
        # Read the CSV file into memory
        with open(EQUIPMENT_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(infile, encoding='utf-8')

        # Validate inputs
        df_filtered = df[df['Item #'] == item]

        # Update the specific cell
        df_filtered['Condition'] = input("Enter New Condition: ")
        if df_filtered['Condition'] == '0':
            df_filtered['Condition'] = df_filtered['Condition']
        else:
            df_filtered['Condition'] = input("Enter New Condition: ")

        print(f"Successfully updated item number {item}, column '{'Condition'}' with value '{condition}'.")
    except FileNotFoundError:
        print(f"Error: File '{EQUIPMENT_FILE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def inventory_tool_room(EQUIPMENT_FILE):
    EQUIPMENT_FILE = 'database/Equipment.csv'  # input file path and desired output file path
    columns_to_keep = ['Item #', 'Item Info', 'ToolRoomID', 'Condition']
    toolroom = int(input("Enter Tool Room ID: "))
    try:
      # Read the CSV file into a DataFrame
        df = pd.read_csv(EQUIPMENT_FILE)

        # Check if the specified column exists
        missing_columns = [col for col in columns_to_keep if col not in df.columns]
        if missing_columns:
            print(f"Error: The following columns are missing in the CSV file: {missing_columns}")
            return
    # Select only the desired columns
        df = df[columns_to_keep]

    # Filter rows where the column matches the given value
        filtered_df = df[df['ToolRoomID'] == toolroom]

    # Check if any rows match the item
        if filtered_df.empty:
            print(f"No rows found with '{'ToolRoomID'}' equal to '{toolroom}'.")
        else:
            print("Filtered rows:")
            print(filtered_df)

    except FileNotFoundError:
        print(f"Error: File '{EQUIPMENT_FILE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# other functions
# count workorders
def count_rows_csv_WorkOrder(WORK_ORDER_FILE): # this shows before main file function
    try:
        with open('database/WorkOrder.csv', mode='r') as file:
            reader = csv.reader(WORK_ORDER_FILE)
            row_count = sum(1 for row in reader)  # Count rows
        return row_count - 1  # Subtract 1 if the first row is a header
    except FileNotFoundError:
        print(f"Error: File '{WORK_ORDER_FILE}' not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


#print(f"Current WorkOrders: {count_rows_csv_WorkOrder(WORK_ORDER_FILE)}")


def add_work_order(WORK_ORDER_FILE):
  # New row to append (list of values)
    WORK_ORDER_FILE = 'database/WorkOrder.csv'
    count = count_rows_csv_WorkOrder(WORK_ORDER_FILE)+1  #this should count the rows in the csv file and add 1 to the last row
    comment = input("Enter Work Order Comments: ")
    employee = input("Enter EmployeeID: ")
    location = input("Select Location ID: ")
    job_type = input("Select Job Type: ")
  #    Appends a new row to an existing CSV file.
    new_row = [count, comment, employee, location, job_type]

    try:
        # Open the file in append mode ('a') and set newline='' to avoid extra blank lines
        with open('database/WorkOrder.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)  # Append the new row
            print(f"Row {new_row} successfully added to {WORK_ORDER_FILE}.")
    except Exception as e:
        print(f"Error: {e}")
