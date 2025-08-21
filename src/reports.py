import csv
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
def auditor_report():
    print("")



def reports_menu():
    print("")
def live_reports():

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
    print("")
def inventory_reports():
    print("")