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
        
def count_rows_trans(TRANSACTIONS_FILE): # this count pervious transactions
    try:
        with open('database/Equipment.csv', mode='r') as file:
            reader = csv.reader(file)
            row_count = sum(1 for row in reader)  # Count rows
        return row_count - 1  # Subtract 1 if the first row is a header
    except FileNotFoundError:
        print(f"Error: File '{TRANSACTIONS_FILE}' not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

def transactions(TRANSACTIONS_FILE):
    TRANSACTIONS_FILE = 'database/Transactions.csv'# add transaction
    transactionID = count_rows_trans(TRANSACTIONS_FILE)+1  #this counts the transactions and adds 1
    employee = input("Enter EmployeeID: ")
    equiptoolitem = input("Enter Equip Tool Item ID 10 didgets or 0 for none: ")
    material = input("Enter Material ID or 0 for none: ")
    fromloc = input("Enter Current Location 'ToolRoom 1 or 2' 'Employee 3' 'Warehouse 4 or 5': ")
    toloc = input("Enter New Location: ")
    transtype = input("Enter 1 for check-in or 2 for check-out: ")
    transdate = input("Enter Transaction Date as M/D/YYYY: ")
    workorder = input("Enter Work Order ID: ")
        #    Appends a new row to an existing CSV file.
    new_transaction_row = [transactionID, employee, equiptoolitem, material, fromloc, toloc, transtype, transdate, workorder]

    try:
        # Open the file in append mode ('a') and set newline='' to avoid extra blank lines
        with open('database/Transactions.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_transaction_row)  # Append the new row
        print(f"Row {new_transaction_row} successfully added to {TRANSACTIONS_FILE}.")
    except Exception as e:
        print(f"Error: {e}")

def tool_location_update(EQUIPMENT_FILE):
    EQUIPMENT_FILE = 'database/Equipment.csv'
    item = int(input("Enter Item Number: "))
    toolroom = input("Enter New Tool Room Name: ")
    employee = int(input("Enter EmployeeID: "))
    toolroomid = int(input("Enter New Tool Room ID: "))
    condition = input("Enter New Condition: ")
    try:
        # Read the CSV file into memory
        with open(EQUIPMENT_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(infile, encoding='utf-8')

        # Validate inputs
        df_filtered = df[df['Item #'] == item]
        print(df_filtered)
        
        # Update the specific cell
        if toolroom != '0':
            df.loc[df['Item #'] == item, 'ToolRoomName'] = toolroom

        if employee != '0':
            df.loc[df['Item #'] == item, 'EmployeeID'] = employee
        else:
            df.loc[df['Item #'] == item, 'EmployeeID'] = '0'

        if toolroomid != '0':
            df.loc[df['Item #'] == item, 'ToolRoomID'] = toolroomid

        if condition != '0':
            df.loc[df['Item #'] == item, 'Condition'] = condition
            
            # Save the DataFrame to CSV file
        df.to_csv(EQUIPMENT_FILE, index=False)

        print(f"Successfully updated item number {item}, column '{'Condition'}' with value '{condition}'.")
    except FileNotFoundError:
        print(f"Error: File '{EQUIPMENT_FILE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

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
        df_filtered = df[df['EmployeeID'] == employee]

        # Check if any rows match the item
        if df_filtered.empty:
            print(f"No rows found with '{'EmployeeID'}' equal to '{employee}'.")
        else:
            print("Filtered rows:")
            print(df_filtered)

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
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    hiredate = input("Enter Hire Date as YYYY-MM-DD: ")
    jobtitle = int(input("Enter Job Title ID 1-112: "))
    phone = input("Enter Phone Number as (###)###-####: ")
    email = input("Enter Email Address: ")
    manager = int(input("Enter Manager ID: "))
    try:
            # Open the file for reading
        with open(EMPLOYEE_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(EMPLOYEE_FILE)
            
            # Select rows where 'EmployeeID' column equals provided value
            df_filtered = df[df['EmployeeID'] == employeeID]
            print(df_filtered)
            # Update the row with new values
            # Update the specific cell
            if fname != '0':
                df.loc[df['EmployeeID'] == employeeID, 'F_Name'] = fname

            if df_filtered['L_Name'] != '0':
                df.loc[df['EmployeeID'] == employeeID, 'L_Name'] = lname

            if hiredate != '0':
                df.loc[df['EmployeeID'] == employeeID, 'HireDate'] = hiredate

            if jobtitle != '0':
                df.loc[df['EmployeeID'] == employeeID, 'JobTitleID'] = jobtitle

            if phone != '0':
                df.loc[df['EmployeeID'] == employeeID, 'Phone'] = phone

            if email != '0':
                df.loc[df['EmployeeID'] == employeeID, 'Email'] = email

            if manager != '0':
                df.loc[df['EmployeeID'] == employeeID, 'ManagerID'] = manager

            # Save the DataFrame to CSV file
            df.to_csv(EMPLOYEE_FILE, index=False)

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
        df_filtered = df[df['Condition'] == condition]

        # Check if any rows match the condition
        if df_filtered.empty:
            print(f"No rows found with '{'Condition'}' equal to '{condition}'.")
        else:
            print("Filtered rows:")
            print(df_filtered)

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


#procurement functions Clayton
  # see inventory_tool_room function in equipment functions section
def update_inventory_tool(EQUIPMENT_FILE):
    EQUIPMENT_FILE = 'database/Equipment.csv'  # input file path and desired output file path
    item = input("Enter Item Number: ")
    equipnumber = input("Enter Equipment Number: ")
    equiptype = input("Enter Equipment Type: ")
    toolnumber = input("Enter Tool Number: ")
    equiptoolID = input("Enter Equip Tool ID: ")
    toolspecifics = input("Enter Tool Specifics: ")
    equiptoolitemID = input("Enter Equip Tool Item ID: ")
    iteminfo = input("Enter Item Info: ")
    toolboxtype = input("Enter Tool Box Type: ")
    jobID = input("Enter Job ID: ")
    toolboxID = input("Enter Tool Box ID: ")
    toolboxjobID = input("Enter Tool Box Job ID: ")
    toolroomname = input("Enter Tool Room Name: ")
    employeeID = input("Enter Employee ID: ")
    toolroomID = input("Enter Tool Room ID: ")
    condition = input("Enter Condition: ")
    certificationID = input("Enter Certification ID: ")
    certificationID2 = input("Enter Certification ID 2: ")
    price = input("Enter Price: ")
    item2 = input("Enter New Item Number: ")
    try:
        # Open the file for reading
        with open(EQUIPMENT_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(EQUIPMENT_FILE)
            
            # Select rows where 'Item #' column equals provided value
            df_filtered = df[df['Item #'] == item]
            print(df_filtered)
            # Update the row with new values

            if equipnumber != '0':
                df.loc[df['Item #'] == item, 'Equipment #'] = equipnumber

            if equiptype != '0':
                df.loc[df['Item #'] == item, 'Equipment Type'] = equiptype

            if toolnumber != '0':
                df.loc[df['Item #'] == item, 'Tool #'] = toolnumber

            if equiptoolID != '0':
                df.loc[df['Item #'] == item, 'EquipToolID'] = equiptoolID

            if toolspecifics != '0':
                df.loc[df['Item #'] == item, 'Tool Specifics'] = toolspecifics

            if equiptoolitemID != '0':
                df.loc[df['Item #'] == item, 'EquipToolItemID'] = equiptoolitemID

            if iteminfo != '0':
                df.loc[df['Item #'] == item, 'Item Info'] = iteminfo
            
            if toolboxtype != '0':
                df.loc[df['Item #'] == item, 'ToolBox Type'] = toolboxtype

            if jobID != '0':
                df.loc[df['Item #'] == item, 'JobID'] = jobID

            if toolboxID != '0':
                df.loc[df['Item #'] == item, 'ToolBoxID'] = toolboxID

            if toolboxjobID != '0':
                df.loc[df['Item #'] == item, 'ToolBoxJobID'] = toolboxjobID

            if toolroomname != '0':
                df.loc[df['Item #'] == item, 'ToolRoomName'] = toolroomname

            if employeeID != '0':
                df.loc[df['Item #'] == item, 'EmployeeID'] = employeeID

            if toolroomID != '0':
                df.loc[df['Item #'] == item, 'ToolRoomID'] = toolroomID

            if condition != '0':
                df.loc[df['Item #'] == item, 'Condition'] = condition

            if certificationID != 'N':
                df.loc[df['Item #'] == item, 'CertificationID'] = certificationID

            if certificationID2 != 'N':
                df.loc[df['Item #'] == item, 'CertificationID2'] = certificationID2

            if price != '0':
                df.loc[df['Item #'] == item, 'Price'] = price

            df.to_csv(EQUIPMENT_FILE, index=False)
            print(f"Item number '{item}' has been updated. Confirm item number by entering 0 or update item number.")
            df_filtered = df[df['EquipToolItemID'] == equiptoolitemID]
            
            if item2 != '0':
                df.loc[df['EquipToolItemID'] == equiptoolitemID, 'Item #'] = item2

            # Save the DataFrame to CSV file
            df.to_csv(EQUIPMENT_FILE, index=False)
        print(f"Item number '{item}' has been updated. New item number is '{item2}'.")
    except FileNotFoundError:
        print(f"Error: The file '{MATERIAL_LOC_FILE}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#Warehouse functions
def material_update():
    MATERIAL_LOC_FILE = 'database/MaterialInventory.csv'  # input file path and desired output file path
    materialID = int(input("Enter Material ID to update: ")) # employeeID to update
    loc_id = input("Enter LocationID: ")
    loc_name = input("Enter Location Name: ")
    job_id = int(input("Enter JobID: "))
    material_name = input("Enter Material Name: ")
    quantity = int(input("Enter New Quantity Press N to Skip: "))
    
    try:
            # Open the file for reading
        with open(MATERIAL_LOC_FILE, mode='r', newline='', encoding='utf-8') as infile:
            df = pd.read_csv(MATERIAL_LOC_FILE)

            # Select rows where 'LocationID' column equals provided value
            df_filtered = df[df['MaterialID'] == materialID]
            print(df_filtered)
            # Update the row with new values

            if loc_id != '0':
                df.loc[df['MaterialID'] == materialID, 'LocationID'] = loc_id

            if loc_name != '0':
                df.loc[df['MaterialID'] == materialID, 'LocationName'] = loc_name

            if job_id != '0':
                df.loc[df['MaterialID'] == materialID, 'JobID'] = job_id

            if material_name != '0':
                df.loc[df['MaterialID'] == materialID, 'MaterialName'] = material_name

            if quantity != 'N':
                df.loc[df['MaterialID'] == materialID, 'Quantity'] = quantity
            
            # Save the DataFrame to CSV file
            df.to_csv(MATERIAL_LOC_FILE, index=False)

            print(f"Material number '{materialID}' has been updated.")
    except FileNotFoundError:
        print(f"Error: The file '{MATERIAL_LOC_FILE}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def inventory_materials(MATERIAL_LOC_FILE):  
    MATERIAL_LOC_FILE = 'database/MaterialInventory.csv'  # input file path and desired output file path
    location = int(input("Enter Location ID to view: ")) # employeeID to update
    columns_to_keep = ['LocationID', 'LocationName', 'JobID', 'MaterialName', 'Quantity']
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
        if df_filtered.empty:
            print(f"No rows found with '{'LocationID'}' equal to '{location}'.")
        else:
            print("Filtered rows:")
            print(df_filtered)
    except FileNotFoundError:
        print(f"Error: The file '{MATERIAL_LOC_FILE}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



#Equipment functions Brandon

def equipment_status(EQUIPMENT_FILE='database/Equipment.csv'): #see inventory_condition_tool function or Claytons File
    columns_to_show = ['Item #', 'Item Info', 'Condition', 'ToolRoomName', 'EmployeeID']
    # Read the CSV file into a DataFrame
    try:
        df = pd.read_csv(EQUIPMENT_FILE, encoding='utf-8')
        # Check if the specified columns exist
        missing_columns = [col for col in columns_to_show if col not in df.columns]
        #if any columns are missing, print an error message and return
        if missing_columns:
            print(f"Error: The following columns are missing in the CSV file: {missing_columns}")
            return
        print(df[columns_to_show])
    # if the file is not found, print an error message
    except FileNotFoundError:
        print(f"Error: File '{EQUIPMENT_FILE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


        

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
        print(df_filtered)
        # Update the specific cell
        if condition != '0':
            df.loc[df['Item #'] == item, 'Condition'] = condition

            # Save the DataFrame to CSV file
        df.to_csv(EQUIPMENT_FILE, index=False)

        print(f"Successfully updated item number {item}, column '{'Condition'}' with value '{condition}'.")
    except FileNotFoundError:
        print(f"Error: File '{EQUIPMENT_FILE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def inventory_tool_room(EQUIPMENT_FILE):
    EQUIPMENT_FILE = 'database/Equipment.csv'  # input file path and desired output file path
    columns_to_keep = ['EquipToolItemID', 'Item #', 'Item Info', 'ToolRoomID', 'Condition']
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
