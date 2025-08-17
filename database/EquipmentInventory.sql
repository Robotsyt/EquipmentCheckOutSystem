CREATE VIEW LocationsAll AS
SELECT L.LocationID, W.WarehouseName, L.WarehouseID, TR.ToolRoomName, L.ToolRoomID, L.ToolBoxJobID, S.SiteID, S.Building, S.FloorLevel, S.Room
FROM location L
LEFT JOIN toolroom TR ON TR.ToolRoomID = L.ToolRoomID
LEFT JOIN site S ON S.SiteID = L.SiteID
LEFT JOIN warehouse W ON W.WarehouseID =L.WarehouseID;

CREATE VIEW EquipmentInventory AS
SELECT I.EquipToolItemID, I.ItemInfo, TRT.ToolRoomID, ETB.ToolBoxJobID, ETB.EmployeeID
FROM item I
LEFT JOIN toolroomtools TRT ON I.EquipToolItemID = TRT.EquipToolItemID
LEFT JOIN toolboxtools TBT ON I.EquipToolItemID = TBT.EquipToolItemID
LEFT JOIN employeetoolbox ETB ON TBT.ToolBoxJobID = ETB.ToolBoxJobID;

CREATE VIEW EquipmentLocation AS
SELECT EI.EquipToolItemID, EI.ItemInfo, LA.LocationID, LA.WarehouseName, LA.WarehouseID, LA.ToolRoomName, LA.ToolRoomID, EI.ToolRoomID, LA.ToolBoxJobID, EI.ToolBoxJobID, EI.EmployeeID, LA.SiteID, LA.Building, LA.FloorLevel, LA.Room
FROM EquipmentInventory EI
LEFT JOIN LocationsAll LA ON LA.ToolRoomID = EI.ToolRoomID OR LA.ToolBoxJobID = EI.ToolBoxJobID;
