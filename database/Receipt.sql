CREATE VIEW Receipt AS
SELECT Employee.EmployeeID AS TransactionEmployee, Employee.F_Name, Employee.L_Name, JobTitle.JobTitle, WorkOrder.WorkOrderID, WorkOrder.EmployeeID AS OriginalEmployee, Transactions.TransTypeID, TransactionTypes.TransType, Transactions.TransactionDate, Transactions.TransactionID, Transactions.EquipToolItemID, Item.ItemInfo, Transactions.MaterialID, Materials.MaterialName
FROM Employee
JOIN JobTitle ON Employee.Job_TitleID = JobTitle.Job_TitleID
LEFT JOIN WorkOrder ON WorkOrder.EmployeeID = Employee.EmployeeID
LEFT JOIN Transactions ON WorkOrder.WorkOrderID = Transactions.WorkOrderID
LEFT JOIN TransactionTypes ON Transactions.TransTypeID = TransactionTypes.TransTypeID
LEFT JOIN Item ON Item.EquipToolItemID = Transactions.EquipToolItemID
LEFT JOIN Materials ON Transactions.MaterialID = Materials.MaterialID;


SELECT *
FROM Receipt
