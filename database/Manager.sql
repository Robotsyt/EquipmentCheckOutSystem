CREATE VIEW Manager AS
SELECT E.EmployeeID, E.F_Name, E.L_Name, JT.JobTitle, JT.JobID, JT.JobSkillLevelID
FROM Employee E
JOIN JobTitle JT ON E.Job_TitleID = JT.Job_TitleID;

SELECT *
FROM Manager