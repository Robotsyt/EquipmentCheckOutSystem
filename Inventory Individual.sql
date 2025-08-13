CREATE VIEW ToolBoxInventory AS
SELECT E.EmployeeID, E.F_Name, E.L_Name, JT.JobTitle, ET.EquipToolItemID AS Equipment, ETB.ToolBoxJobID, TBT.EquipToolItemID AS ToolBoxEquipment, Item.ItemInfo
FROM Employee E
JOIN JobTitle JT ON E.Job_TitleID = JT.Job_TitleID
LEFT OUTER JOIN EmployeeTools ET ON ET.EmployeeID = E.EmployeeID
JOIN EmployeeToolBox ETB ON ETB.EmployeeID = E.EmployeeID
JOIN ToolBoxTools TBT ON TBT.ToolBoxJobID = ETB.ToolBoxJobID
JOIN Item ON ET.EquipToolItemID = Item.EquipToolItemID OR TBT.EquipToolItemID = Item.EquipToolItemID;


SELECT *
FROM ToolBoxInventory;

