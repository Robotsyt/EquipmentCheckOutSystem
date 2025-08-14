CREATE VIEW Receipt AS
SELECT Employee.EmployeeID AS TransactionEmployee, Employee.F_Name, Employee.L_Name, JobTitle.JobTitle, WorkOrder.WorkOrderID, WorkOrder.EmployeeID AS OriginalEmployee, Transactions.TransTypeID, TransactionTypes.TransType, Transactions.TransactionDate, Transactions.TransactionID, Transactions.EquipToolItemID, Item.ItemInfo, Transactions.MaterialID, Materials.MaterialName
FROM Employee
JOIN JobTitle ON Employee.Job_TitleID = JobTitle.Job_TitleID
JOIN WorkOrder ON WorkOrder.EmployeeID = Employee.EmployeeID
JOIN Transactions ON WorkOrder.WorkOrderID = Transactions.WorkOrderID
JOIN TransactionTypes ON Transactions.TransTypeID = TransactionTypes.TransTypeID
JOIN Item ON Item.EquipToolItemID = Transactions.EquipToolItemID
JOIN Materials ON Transactions.MaterialID = Materials.MaterialID;


SELECT *
FROM Receipt