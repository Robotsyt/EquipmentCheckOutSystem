# count employees
def count_rows_csv(file_path): # this shows before main file function
    try:
        with open('database/Employee.csv', mode='r') as file:
            reader = csv.reader(file)
            row_count = sum(1 for row in reader)  # Count rows
        return row_count - 1  # Subtract 1 if the first row is a header
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage
file_path = 'database/Employee.csv'
print(f"Total employees: {count_rows_csv(file_path)}")


def add_employee(file_path, new_row):

    try:
        # Open the file in append mode ('a') and set newline='' to avoid extra blank lines
        with open('database/Employee.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)  # Append the new row
        print(f"Row {new_row} successfully added to {file_path}.")
    except Exception as e:
        print(f"Error: {e}")

# New row to append (list of values)
value1 = count_rows_csv(file_path)+1  #this should count the rows in the csv file and add 1 to the last row
value2 = input("Enter First Name: ")
value3 = input("Enter Last Name: ")
value4 = input("Enter Hire Date as YYYY-MM-DD: ")
value5 = input("Enter Job Title ID 1-112: ")
value6 = input("Enter Phone Number as (###)###-####: ")
value7 = input("Enter Email Address: ")
value8 = input("Enter Manager ID: ")
#    Appends a new row to an existing CSV file.
new_row = [value1, value2, value3, value4, value5, value6, value7, value8]
# Path to the CSV file
csv_file = 'database/Employee.csv'
# Append the new row to the CSV file
add_employee(csv_file, new_row)


def remove_employee(input_file, output_file, column_index, value_to_remove): #this function removes too many employees from the csv file also appears before main menu function
    """
    Removes rows from a CSV file where the value in the specified column matches the given value.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        column_index (int): Index of the column to check (0-based).
        value_to_remove (str): Value to match for row removal.
    """
    try:
        # Open the input file for reading
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)

            # Read the header (if present)
            header = next(reader, None)

            # Open the output file for writing
            with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)

                # Write the header to the output file (if present)
                if header:
                    writer.writerow(header)

                # Iterate through rows and write only those that don't match the condition
                for row in reader:
                    if row[column_index] != value_to_remove:
                        writer.writerow(row)

        print(f"Employee number '{value_to_remove}' has been removed.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IndexError:
        print(f"Error: Column index {column_index} is out of range.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_csv = 'database/Employee.csv'  # input file path
output_csv = 'database/Employee.csv'  # desired output file path
column_to_check = 1  # Replace with the column index (0-based)
removeemployeeID = input("Enter Employee ID to remove: ")
value_to_remove = 'removeemployeeID'  # value to remove

remove_rows(input_csv, output_csv, column_to_check, value_to_remove)

def update_employee():
    pass






