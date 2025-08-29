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
    
  
    
def email_report():
    """Simulates compiling a report and 'emailing' it to stakeholders."""
    def progress(msg, steps=3, delay=0.4):
        print(msg, end="", flush=True)
        for _ in range(steps):
            time.sleep(delay)
            print(".", end="", flush=True)
        print()

    print("\n===| Email Report |===")
    time.sleep(0.5)

    # Step 1: "Access" data sources (and lightly inspect them for realism)
    sources = {
        "Employees": "database/Employee.csv",
        "Equipment": EQUIPMENT_FILE,
        "Materials": MATERIAL_LOC_FILE,
    }

    counts = {}
    for label, path in sources.items():
        progress(f"Accessing {path}")
        try:
            with open(path, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader, None)
                row_count = sum(1 for _ in reader)
                counts[label] = {"rows": row_count, "columns": len(header) if header else 0}
        except FileNotFoundError:
            counts[label] = {"rows": 0, "columns": 0}
            print(f"  ⚠️  {label} file not found at '{path}'. Continuing with defaults.")
        except Exception as e:
            counts[label] = {"rows": 0, "columns": 0}
            print(f"  ⚠️  Could not read {label} ({e}). Continuing with defaults.")
        time.sleep(0.3)

    # Step 2: "Compile" a quick summary
    progress("Compiling report data", steps=4, delay=0.3)
    print("Summary:")
    for label, meta in counts.items():
        print(f"  - {label}: {meta['rows']} rows, {meta['columns']} columns")

    # Step 3: "Prepare" recipients and subject
    recipients_to = [
        "operations@moroathletics.com",
        "warehouse@moroathletics.com",
    ]
    recipients_cc = [
        "auditor@moroathletics.com",
        "finance@moroathletics.com",
    ]
    subject = "Daily Inventory & Materials Report (Simulation)"
    print("\nComposed Email:")
    print(f"  Subject: {subject}")
    print(f"  To: {', '.join(recipients_to)}")
    print(f"  Cc: {', '.join(recipients_cc)}")

    # Step 4: "Send" the email
    progress("Establishing secure SMTP connection")
    print("  ✔ Connection established (mock)")
    progress("Dispatching email to recipients", steps=5, delay=0.2)
    print(f"✅ Email successfully sent to: {', '.join(recipients_to)}")
    print(f"ℹ️  Cc recipients: {', '.join(recipients_cc)}")
   


