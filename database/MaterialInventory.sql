CREATE VIEW MaterialInventory AS
SELECT M.MaterialID, M.MaterialName, ML.Quantity, W.WarehouseName, L.LocationID
FROM materials M
JOIN materiallocations ML ON M.MaterialID = ML.MaterialID
LEFT JOIN warehouse W ON W.WarehouseID =ML.WarehouseID
LEFT JOIN location L ON L.WarehouseID = ML.WarehouseID;

SELECT *
FROM MaterialInventory;
