# Reports
# cursor.execute("SELECT * FROM table_name") #Selects all in table
# cursor.execute("SELECT * FROM table_name WHERE column_name = input") #Selects all columns in table restricts rows (verify please)


# Historical Transactions
def inventories():
    while True:
        time.sleep(3)
        print("===| Select Transactions |===")
        print("1.  ALL")
        value1 = input()
rows = cursor.fetchall()
    if value1 == "1":
        cursor.execute("SELECT * FROM Transactions")
        print("2.  TransactionID")
        value1 = input()
rows = cursor.fetchall()
    if value1 == "2":
        value2 = input("Enter TransactionID: ")
        cursor.execute("SELECT * FROM Transactions WHERE TransactionID = value2")
        print("3.  EmployeeID")
        value1 = input()
rows = cursor.fetchall()
    if value1 == "3":
        value2 = input("Enter EmployeeID: ")
        cursor.execute("SELECT * FROM Transactions WHERE EmployeeID = value2")
        print("4.  EquipToolItemID")
        value1 = input()
rows = cursor.fetchall()
    if value1 == "4":
        value2 = input("Enter EquipToolItemID: ")
        cursor.execute("SELECT * FROM Transactions WHERE EquipToolItemID = value2")
        print("5.  MaterialID")
        value1 = input()
rows = cursor.fetchall()
    if value1 == "5":
        value2 = input("Enter MaterialID: ")
        cursor.execute("SELECT * FROM Transactions WHERE MaterialID = value2")
        print("6.  TransTypeID")
        value1 = input()
rows = cursor.fetchall()
    if value1 == "6":
        value2 = input("Enter TransTypeID: ")
        cursor.execute("SELECT * FROM Transactions WHERE TransTypeID = value2")
        print("7.  TransactionDate")
        value1 = input()
rows = cursor.fetchall()
    if value1 == "7":
        value2 = input("Enter TransactionDate as YYYY-MM-DD: ")
        cursor.execute("SELECT * FROM Transactions WHERE TransactionDate = value2")
        print("8.  WorkOrderID")
        value1 = input()
rows = cursor.fetchall()
    if value1 == "8":
        value2 = input("Enter WorkOrderID: ")
        cursor.execute("SELECT * FROM Transactions WHERE WorkOrderID = value2")


# Lost Stolen Damaged Cost

# Individual Lost Stolen Damaged Cost

# Inventories
def inventories():
    while True:
        time.sleep(3)
        print("===| Inventory Menu |===")
        print("1.  Equipment")
        print("2.  Materials")
        print("3.  Individual")

# Equipment Inventory
value1 = input("Press 1 for all ToolRoom Equipment, Press 2 for Main ToolRoom Equipment, Press 3 for Quick ToolRoom Equipment: ")
rows = cursor.fetchall()
if value1 == "1":
    cursor.execute("SELECT * FROM EquipmentInventory") #All warehouses
elif value1 == "2":
    cursor.execute("SELECT * FROM EquipmentInventory WHERE LocationID = 3") #ToolRoom Main
elif value1 == "3":
    cursor.execute("SELECT * FROM EquipmentInventory WHERE LocationID = 4") #ToolRoom Quick
else:
    print("Invalid selection. Please try again.")
    input("Press Enter to continue ...")
print(rows)
mydb.commit()
cursor.close()

# Material Inventory
value1 = input("Press 1 for all Materials, Press 2 for Main Warehouse Materials, Press 3 for Quick Warehouse Materials: ")
rows = cursor.fetchall()
if value1 == "1":
    cursor.execute("SELECT * FROM MaterialInventory") #All warehouses
elif value1 == "2":
    cursor.execute("SELECT * FROM MaterialInventory WHERE WarehouseID LIKE '1%'") #Warehouse Main
elif value1 == "3":
    cursor.execute("SELECT * FROM MaterialInventory WHERE WarehouseID LIKE '2%'") #Warehouse Quick
else:
    print("Invalid selection. Please try again.")
    input("Press Enter to continue ...")
print(rows)
mydb.commit()
cursor.close()

# Individual Equipment
value1 = input("Please verify EmployeeID: ")
rows = cursor.fetchall()
cursor.execute("SELECT * FROM ToolBoxInventory WHERE EmployeeID = value1")
print(rows)
mydb.commit()
cursor.close()

# Employee Certifications
value1 = input("Please verify EmployeeID: ")
rows = cursor.fetchall()
cursor.execute("SELECT * FROM EmployeeCertNames WHERE EmployeeID = value1")
print(rows)
mydb.commit()
cursor.close()

# Employee Authorized Tools
value1 = input("Please verify EmployeeID: ")
rows = cursor.fetchall()
cursor.execute("SELECT * FROM EmployeeCertifiedTools WHERE EmployeeID = value1")
print(rows)
mydb.commit()
cursor.close()

# Last known location of Equipment
value1 = input("Enter EquipmentToolItemID: ")
rows = cursor.fetchall()
cursor.execute("SELECT * FROM EquipmentInventory WHERE EquipmentToolItemID = value1")
print(rows)
mydb.commit()
cursor.close()