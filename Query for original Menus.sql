-- SQL Merge Info for original validate menus

SELECT Employee.EmployeeID, JobTitle.Job_TitleID, JobTitle.JobID, JobTitle.JobSkillLevelID
FROM Employee
INNER JOIN JobTitle ON Employee.Job_TitleID = JobTitle.Job_TitleID;

-- JobID 1-18 Maintenance, 19 HR, 20 Finance, 21 Auditor, 22 Safety, 23 Project Management, 24 Administration, 25 Procurement, 26 Warehouse, 27 Equipment(Toolroom), 28 IT, 29 Misc other non related employees
-- JobSkillLeveID 1-3 Managers, 4 Supervisor, 5 Expert(Worker), 6 Trades Helpers, 7 Interns