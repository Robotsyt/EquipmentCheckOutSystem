CREATE VIEW EmployeeCertifiedTools AS
SELECT ECN.EmployeeID, ECN.CertificationName, ECN.CertificationID, CT.EquipmentToolID, CT.CertificationID
FROM EmployeeCertNames ECN
INNER JOIN CertificationTools CT ON ECN.CertificationID = CT.CertificationID
JOIN Tool ON Tool.EquipmentToolID =  CT.EquipmentToolID;

SELECT *
FROM EmployeeCertifiedTools;