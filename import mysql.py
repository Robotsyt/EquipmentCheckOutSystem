import mysql.connector #for mysql

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database=yourdatabase" # Optional
)

#Cursor Examples
#SELECT (search) script
cursor.execute("SELECT * FROM table_name") #Selects all in table
cursor.execute("SELECT * FROM table_name WHERE column_name = input") #Selects all columns in table restricts rows (verify please)
#INSERT (add) script
cursor.execute("INSERT INTO table_name (column_name, colum_name2) VALUES (%s, %s)", ("value1, "value2"))
#DELETE (remove) script
cursor.execute("DELETE FROM table_name WHERE (column_name = input)")

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