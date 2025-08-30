import csv
import loaders
import pandas as pd
from loaders import EQUIPMENT_FILE, MATERIAL_LOC_FILE
import time

#CSV reader
def load_data(filename):
    my_list = []  # Initialize an empty list to store rows
    with open (filename, 'r') as identify:       # Open the filepath to the specified CSV file
        identify_data = csv.reader(identify)  # Create a CSV reader object
        next(identify_data) # Skip the header information

        for row in identify_data:
            my_list.append(row)  # Append each row to the list
        return my_list  # Return the list of rows
#reports function loader

#Auditor Function
def auditor_report(): # done
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        print("===| Auditor Reports |===")  # Print the Auditor Reports menu header
        print("1.  Inventory By Employee")  # Option 1: Inventory by employee
        print("2.  Inventory By Condition")  # Option 2: Inventory by condition
        print("3.  Inventory By Tool Room")  # Option 3: Inventory by tool room
        print("4.  Inventory By Materials")  # Option 4: Inventory by materials

        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == "1":
                loaders.inventory_employee_tool(EQUIPMENT_FILE)  # Call function for inventory by employee
            elif input_value == '2':
                loaders.inventory_condition_tool(EQUIPMENT_FILE)  # Call function for inventory by condition
            elif input_value == '3':
                loaders.inventory_tool_room(EQUIPMENT_FILE)  # Call function for inventory by tool room
            elif input_value == '4':
                loaders.inventory_materials(MATERIAL_LOC_FILE)  # Call function for inventory by materials
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration




def reports_menu(): # done
    while True:
        time.sleep(1)  # Pause for 1 second for user experience
        print("===| Reports |===")  # Print the Reports menu header
        print("1.  Inventory By Employee")  # Option 1: Inventory by employee
        print("2.  Inventory By Condition")  # Option 2: Inventory by condition
        print("3.  Inventory By Tool Room")  # Option 3: Inventory by tool room
        print("4.  Inventory By Materials")  # Option 4: Inventory by materials

        try:
            input_value = input("Select an option: ")  # Prompt user for menu selection
            if input_value == "1":
                loaders.inventory_employee_tool(EQUIPMENT_FILE)  # Call function for inventory by employee
            elif input_value == '2':
                loaders.inventory_condition_tool(EQUIPMENT_FILE)  # Call function for inventory by condition
            elif input_value == '3':
                loaders.inventory_tool_room(EQUIPMENT_FILE)  # Call function for inventory by tool room
            elif input_value == '4':
                loaders.inventory_materials(MATERIAL_LOC_FILE)  # Call function for inventory by materials
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not available. Exiting program.")  # Handle input interruption
        break  # Exit the loop after one iteration



def live_reports(): # done
    associate_id = None  # Initialize associate_id
    first_name = None  # Initialize first_name
    last_name = None  # Initialize last_name
    new_list = load_data('database/Employee.csv')  # Load employee data from CSV
    for row in new_list:
        if len(row) > 0:
            found = True  # Set found flag to True (not used further)
            associate_id = int(row[0])  # Get associate ID
            first_name = row[1] if len(row) > 1 else None   # Get first name (index 1)
            last_name = row[2] if len(row) > 2 else None    # Get last name (index 2)
            print("Employee ID, first name,    Last name")  # Print header
            print(f"{associate_id}   {first_name}     {last_name}")  # Print employee info
def email_report():
    """Simulates compiling a report and 'emailing' it to stakeholders."""
    def progress(msg, steps=3, delay=0.4):
        print(msg, end="", flush=True)  # Print the progress message
        for _ in range(steps):
            time.sleep(delay)  # Wait for the specified delay
            print(".", end="", flush=True)  # Print a dot for each step
        print()  # Newline after progress

    print("\n===| Email Report |===")  # Print the Email Report header
    time.sleep(0.5)  # Brief pause for effect

    # Step 1: "Access" data sources (simulate reading CSVs)
    sources = {
        "Employees": "database/Employee.csv",  # Path to employee data
        "Equipment": EQUIPMENT_FILE,            # Path to equipment data
        "Materials": MATERIAL_LOC_FILE,         # Path to materials data
    }

    counts = {}  # Dictionary to store row/column counts for each source
    for label, path in sources.items():
        progress(f"Accessing {path}")  # Simulate accessing each file
        try:
            with open(path, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader, None)  # Read header row
                row_count = sum(1 for _ in reader)  # Count data rows
                counts[label] = {"rows": row_count, "columns": len(header) if header else 0}  # Store counts
        except FileNotFoundError:
            counts[label] = {"rows": 0, "columns": 0}  # Default if file not found
            print(f"  ⚠️  {label} file not found at '{path}'. Continuing with defaults.")
        except Exception as e:
            counts[label] = {"rows": 0, "columns": 0}  # Default if error
            print(f"  ⚠️  Could not read {label} ({e}). Continuing with defaults.")
        time.sleep(0.3)  # Brief pause for realism

    # Step 2: "Compile" a quick summary of the data
    progress("Compiling report data", steps=4, delay=0.3)
    print("Summary:")
    for label, meta in counts.items():
        print(f"  - {label}: {meta['rows']} rows, {meta['columns']} columns")  # Print summary for each source

    # Step 3: "Prepare" recipients and subject for the email
    recipients_to = [
        "operations@moroathletics.com",
        "warehouse@moroathletics.com",
    ]
    recipients_cc = [
        "auditor@moroathletics.com",
        "finance@moroathletics.com",
    ]
    subject = "Daily Inventory & Materials Report (Simulation)"  # Email subject
    print("\nComposed Email:")
    print(f"  Subject: {subject}")  # Print subject
    print(f"  To: {', '.join(recipients_to)}")  # Print To recipients
    print(f"  Cc: {', '.join(recipients_cc)}")  # Print Cc recipients

    # Step 4: "Send" the email (simulated)
    progress("Establishing secure SMTP connection")  # Simulate connecting to SMTP
    print("  ✔ Connection established (mock)")  # Mock connection established
    progress("Dispatching email to recipients", steps=5, delay=0.2)  # Simulate sending
    print(f"✅ Email successfully sent to: {', '.join(recipients_to)}")  # Print success message
    print(f"ℹ️  Cc recipients: {', '.join(recipients_cc)}")  # Print Cc info
   
