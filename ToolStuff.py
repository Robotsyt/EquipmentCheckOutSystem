#def inventory_tool():
import csv
import pandas as pd

def inventory_employee_tool(file_path, column_name1, value_to_match1):
  try:
      # Read the CSV file into a DataFrame
      df = pd.read_csv(file_path)

      # Check if the specified column exists
      if column_name not in df.columns:
          print(f"Error: Column '{column_name1}' not found in the CSV file.")
          return

      # Filter rows where the column matches the given value
      filtered_df = df[df[column_name1] == value_to_match1]

      # Check if any rows match the condition
      if filtered_df.empty:
          print(f"No rows found with '{column_name1}' equal to '{value_to_match1}'.")
      else:
          print("Filtered rows:")
          print(filtered_df)

  except FileNotFoundError:
      print(f"Error: File '{file_path}' not found.")
  except Exception as e:
      print(f"An error occurred: {e}")


def inventory_condition_tool(file_path, column_name2, value_to_match2):
  try:
      # Read the CSV file into a DataFrame
      df = pd.read_csv(file_path)

      # Check if the specified column exists
      if column_name not in df.columns:
          print(f"Error: Column '{column_name2}' not found in the CSV file.")
          return

      # Filter rows where the column matches the given value
      filtered_df = df[df[column_name2] == value_to_match2]

      # Check if any rows match the condition
      if filtered_df.empty:
          print(f"No rows found with '{column_name2}' equal to '{value_to_match2}'.")
      else:
          print("Filtered rows:")
          print(filtered_df)

  except FileNotFoundError:
      print(f"Error: File '{file_path}' not found.")
  except Exception as e:
      print(f"An error occurred: {e}")

def inventory_tool_room(file_path, column_name3, value_to_match3):
  try:
      # Read the CSV file into a DataFrame
      df = pd.read_csv(file_path)

      # Check if the specified column exists
      if column_name not in df.columns:
          print(f"Error: Column '{column_name3}' not found in the CSV file.")
          return

      # Filter rows where the column matches the given value
      filtered_df = df[df[column_name3] == value_to_match3]

      # Check if any rows match the condition
      if filtered_df.empty:
          print(f"No rows found with '{column_name3}' equal to '{value_to_match3}'.")
      else:
          print("Filtered rows:")
          print(filtered_df)

  except FileNotFoundError:
      print(f"Error: File '{file_path}' not found.")
  except Exception as e:
      print(f"An error occurred: {e}")
# Example usage
file_path = "database/Equipment.csv"  # CSV file path
column_name1 = "EmployeeID"  # column name to filter
employeeID = input("Enter Employee ID: ")
value_to_match1 = employeeID  
column_name2 = "Condition"
condition = input("Enter Condition: ")
value_to_match2 = condition
column_name3 = "ToolRoomID"
tool_room = input("Enter Tool Room 1 or 2: ")
value_to_match3 = tool_room

inventory_employee_tool(file_path, column_name1, value_to_match1)
inventory_condition_tool(file_path, column_name2, value_to_match2)
inventory_tool_room(file_path, column_name3, value_to_match3)


def tool_condition_update(file_path, row_index, column_name, new_value):
    """
        Updates a specific cell in a CSV file.

        :param file_path: Path to the CSV file.
        :param row_index: The row index (0-based) to update.
        :param column_name: The column name to update.
        :param new_value: The new value to set in the specified cell.
        """
    try:
        # Read the CSV file into memory
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)  # Convert to a list of dictionaries
            fieldnames = reader.fieldnames  # Get column names

        # Validate inputs
        if row_index < 0 or row_index >= len(rows):
            raise IndexError("Row index out of range.")
        if column_name not in fieldnames:
            raise ValueError(f"Column '{column_name}' does not exist in the CSV file.")

        # Update the specific cell
        rows[row_index][column_name] = new_value

        # Write the updated data back to the CSV file
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            writer.writerows(rows)  # Write the updated rows

        print(f"Successfully updated row {row_index}, column '{column_name}' with value '{new_value}'.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_file = 'database/Equipment.csv'  # Path to your CSV file
status = input("Enter New Condition: ")
itemID = input("Enter Item ID: ")
tool_condition_update(csv_file, row_index=itemID, column_name='Condition', new_value=status)


