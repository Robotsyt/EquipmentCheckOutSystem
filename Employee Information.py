# Employee Information
# F_Name\L_Name\Hire_Date\Job_TitleID\PhoneNumber\Email\ManagerID

# Add Employee
value1 = input("Please enter Employee First Name: ")
value2 = input("Please enter Employee Last Name: ")
value3 = input("Enter Hire Date/Time as YYYY-MM-DD hh:mm:ss: ")
value4 = input("Please enter Employee JobID: ")
#   JobID
#1	Carpenter
#2	Electricians
#3	Painters
#4	Welders
#5	Plumbers
#6	Special Skills
#7	Lawn And Garden Maintenance
#8	Janitorial And Custodial
#9	Window Cleaning
#10	HVAC and Air conditioning
#11	Fire Systems
#12	Alarm Systems
#13	Flooring
#14	Furniture
#15	Pest Control
#16	Elevator
#17	LockSmith
#18	General Maintenance
#19	HR
#20	Finance
#21	Auditor/Compliance
#22	Safety
#23	Project Manager
#24	Administration
#25	Procurement
#26	WareHouse
#27	Equipment
#28	IT
#29	Other
value5 = input("Please enter Employee JobSkillLevelID: ")
#   JobSkillLevelID
#1	High Level Management
#2	Mid Level Management
#3	Low Level Management
#4	Supervisor
#5	Expert
#6	Trades
#7	Intern
cursor.execute("SELECT Job_TitleID FROM jobtitle WHERE JobID = value4 AND JobSkillLevelID = value5")
print(f"The matching JobTitleID is {JobTitleID}")
value6 = input("Please enter JobTitleID for Employee: ")
value7 = input("Please enter Employee Phone Number: ")
value8 = input("Please enter Employee Email: ")
value9 = input("Please enter Employee ManagerID: ")
cursor.execute("SELECT EmployeeID FROM manager WHERE JobID = value4 AND JobSkillLevelID BETWEEN 1 AND (value5-1)")
print(F"Avaliable manager ID's are {EmployeeID}, {F_Name}, {L_Name}, {JobTitle}.")
cursor.execute("INSERT INTO employee (F_Name, L_Name, Hire_Date, Job_TitleID, PhoneNumber, Email, ManagerID) VALUES (%s, %s, %s, %s, %s, %s, %s)", (value1, value2, value3, value6, value7, value8, value9))
mydb.commit()
cursor.close()

# Remove Employee
value1 = input("Please enter EmployeeID: ")
cursor.execute("SELECT * FROM Employee WHERE EmployeeID = value1")
rows = cursor.fetchall() #all rows
print(f"Employee Info: {rows}")
cursor.execute("DELETE FROM employee WHERE EmployeeID = value1")
mydb.commit()
cursor.close()

# Alter Employee
value1 = input("Please enter Employee ID: )
value2 = input("TBD")
sql = "UPDATE employee SET TBD = %s WHERE EmployeeID = %s"
value = (value2, value1)
cursor.execute(sql, value)

# Employee Certificate
# Add
value1 = input("Please enter EmployeeID: ")
value2 = input("Please select Certification ID: ")
cursor.execute("INSERT INTO Employee_certifications (EmployeeID, CertificationID) VALUES (%s, %s)", (value1, value2))
mydb.commit()
cursor.close()

# Delete
value1 = input("Please enter EmployeeID: ")
cursor.execute("SELECT * FROM EmployeeCertNames WHERE EmployeeID = value1")
rows = cursor.fetchall() #all rows
print(f"Employee Certificate Names: {rows}")
value2 = input("Please select Certification ID: ")
cursor.execute("DELETE FROM employee WHERE EmployeeID = value1 AND CertificationID = value2")
mydb.commit()
cursor.close()

# Alter Do Not Use
'''1	Access Control / Key Control
2	Basic Hand Tool Safety
3	Basic Tester Operation
4	Basic Welding Safety
5	Digital Tool Operation
6	Fall Prevention
7	Fire Safety
8	HAZMat Hadling Certificate
9	Knife Safety
10	Power Tool Safety
11	OSHA 10
12	OSHA 30
13	OSHA 40
15	Master Certified Electronics Technician (CET)
16	EPA HVAC Certification
17	Electrical Technician Certification
19	Project Management Professional (PMP)
22	Facilities Management Certificate (FMC)
23	Facility Management Professional (FMP)
24	Certified Facility Manager (CFM)
25	In-Building Public Safety Communications
26	Electrical Power Testing
27	Fire Alarm Systems
28	Inspection and Testing of Fire Alarm Systems
29	Inspection and Testing of Water-Based Systems
30	Special Hazards Systems
31	Water-Based Systems Layout
32	Technologist certification
33	Certified Lead Carpenter (CLC)
34	Journeyman Carpenter Certification
35	Blueprint Reading
36	Framing
37	Finish Carpentry
38	Building Codes
39	Use of Tools and Equipment
41	Master Electrician Certificate
42	Certified Electrical Safety Worker (CESW)
44	Certified Electrical Safety Technician (CEST)
45	Journeyman Electrician License
46	Certified Automation Professional (CAP)
47	LEED Green Associate
48	Photovoltaic (PV) Installer Certification
49	Certified Energy Manager (CEM)
50	Specialized Technique Certifications
51	Painting Contractor Certification
52	Lead Safety Certification
53	Environmental Certifications
55	Certification for Certified Welding Inspector
58	Certified Welder Certification
59	Certification forÂ Certified Welding Educator
60	Certified Welding Engineer Certification
64	Journeyman Plumber Certification
65	Master Plumber Certification
66	Plumbing Inspector Certification
67	Green Plumber Certification
68	Backflow Prevention Certification
69	ASSE 6010 Installers Certification
70	ASSE 6020 Inspectors Certification
71	ASSE 6040 Maintenance Personnel Certification
72	Landscape Industry Certified Technician
73	LIC Manager
74	LIC Exterior Technician
75	LIC Interior Technician
76	LIC Horticultural Technician
77	LIC Lawn Care Manager
78	LIC Lawn Care Technician
79	Certified Grounds Manager (CGM)
80	Certified Grounds Technician (CGT)
81	Certified Custodial Professional (CCP)
82	IWCA Certified Window Cleaner
83	IWCA Safety Certified Technician
84	IWCA Certified Water-Fed Operator
85	Â IWCA Certified Rope Descent Technician
86	HVAC Excellence Certification
89	Universal R-410A Certification
90	HVAC/R Certification
91	Sheet Metal Certification (SMC)
93	Certified Alarm TechnicianÂ (CAT) Level I
94	Certified Alarm TechnicianÂ (CAT) Level II
95	Certified Fire Alarm TechnicianÂ (CFAT)
96	Certified Fire Alarm DesignerÂ (CFAD)
97	Certified Intrusion TechnicianÂ (CIT)
99	Certified Security SalesÂ (CSS)
100	Certified Security Systems IntegratorÂ (CSSI)
101	Certified Service TechnicianÂ (CST)
102	Certified Systems IntegratorÂ (CSI)
103	Certified Video TechnicianÂ (CVT)
104	Certified Security Project ManagerÂ (CSPM)
105	Associate Protection ProfessionalÂ (APP)
106	Certified Protection ProfessionalÂ (CPP)
107	Physical Security ProfessionalÂ (PSP)
108	Professional Certified InvestigatorÂ (PCI)
110	Floor Technician Certifications
111	Flooring Industry Certification
112	Best Floor Technician Certifications
113	Floor Care Technician (FCT)
114	Furniture Restoration Training
115	General Pest Control Certifications
116	Structural Pest Management
117	Agricultural Pest Management
119	ALOA Certifications'''

