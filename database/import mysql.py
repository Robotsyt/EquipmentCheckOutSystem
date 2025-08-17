

## import mysql.connector to bring sql functions to this python file
import mysql.connector #for mysql
import cursor as cursor #for cursor functions
## this is the connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase" # Optional
)

#Cursor Examples
#SELECT (search) script
cursor.execute("SELECT * FROM table_name") #Selects all in table
cursor.execute("SELECT * FROM table_name WHERE column_name = input") #Selects all columns in table restricts rows (verify please)
#INSERT (add) script
cursor.execute("INSERT INTO table_name (column_name, colum_name2) VALUES (%s, %s)", ("value1", "value2"))
#DELETE (remove) script
cursor.execute("DELETE FROM table_name WHERE (column_name = input)")
#Alter info
sql = "UPDATE table_name SET column_name = %s WHERE column_name = %s"
value = ("column1value", "column2parameter")
cursor.execute(sql, value)
#Add to quantity in database
item_name = "materialname"
quantity = #
price = #.##
add_item_query = "INSERT INTO table_name (item_name, quantity, price) VALUES (%s, %s, %s)"
item_data = (item_name, quantity, price)
mydb.commit()
print(f"{quantity} units of {item_name} added to inventory.")
#Remove from quantity in database
item_to_remove_from = "existingmaterialname"
remove_quantity = #
update_quantity_query = "UPDATE table_name SET quantity = quantity - %s WHERE item_name = %s"
update_data = (remove_quantity, item_to_remove_from)
print(f"{remove_quantity} units of {item_to_remove_from} removed from inventory.")

#results
rows = cursor.fetchall() #all rows
row = cursor.fetchone() #single row
while row:
    print(row)
    row = cursor.fetchone()

#commit changes
mydb.commit()

#close connection
cursor.close()
mydb.close()

