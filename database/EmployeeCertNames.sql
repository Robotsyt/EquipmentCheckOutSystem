CREATE VIEW EmployeeCertNames AS
SELECT EC.EmployeeID, C.CertificationName, EC.CertificationID
FROM Employee_certifications EC
JOIN Certifications C ON EC.CertificationID = C.CertificationID;

SELECT *
FROM EmployeeCertNames