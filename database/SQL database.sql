-- -----------------------------------------------------
-- Table `JobLevel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS JobLevel (
  JobSkillLevelID INT NOT NULL AUTO_INCREMENT,
  SkillLevel VARCHAR(45) NOT NULL,
  PRIMARY KEY (JobSkillLevelID)
  );
  
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/JobLevel.csv"
INTO TABLE JobLevel
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  
  
-- -----------------------------------------------------
-- Table `JobSection`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS JobSection (
  SectionID INT NOT NULL AUTO_INCREMENT,
  Section VARCHAR(45) NOT NULL,
  PRIMARY KEY (SectionID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/JobSection.csv"
INTO TABLE JobSection
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- -----------------------------------------------------
-- Table `JobType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS JobType (
  JobID INT NOT NULL AUTO_INCREMENT,
  JobType VARCHAR(45) NOT NULL,
  PRIMARY KEY (JobID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/JobType.csv"
INTO TABLE JobType
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- -----------------------------------------------------
-- Table `JobTitle`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS JobTitle (
  Job_TitleID INT NOT NULL AUTO_INCREMENT,
  JobTitle VARCHAR(45) NOT NULL,
  JobID INT NOT NULL,
  JobSkillLevelID INT NOT NULL,
  SectionID INT NOT NULL,
  FOREIGN KEY (JobID) REFERENCES JobType (JobID),
  FOREIGN KEY (JobSkillLevelID) REFERENCES JobLevel (JobSkillLevelID),
  FOREIGN KEY (SectionID) REFERENCES JobSection (SectionID),
  PRIMARY KEY (Job_TitleID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/JobTitle.csv"
INTO TABLE JobTitle
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- -----------------------------------------------------
-- Table `Employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Employee (
  EmployeeID INT NOT NULL AUTO_INCREMENT,
  F_Name VARCHAR(45) NULL,
  L_Name VARCHAR(45) NULL,
  Hire_Date DATETIME NULL,
  Job_TitleID INT NOT NULL,
  PhoneNumber VARCHAR(15) NOT NULL,
  Email VARCHAR(45) NOT NULL,
  ManagerID INT, 
  PRIMARY KEY (EmployeeID),
  FOREIGN KEY (Job_TitleID) REFERENCES JobTitle (Job_TitleID),
  CONSTRAINT FK_ManagerID FOREIGN KEY (ManagerID) REFERENCES Employee (EmployeeID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Employee.csv"
INTO TABLE Employee
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- -----------------------------------------------------
-- Table `Certifications`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Certifications (
  CertificationID INT NOT NULL AUTO_INCREMENT,
  CertificationType VARCHAR(45) NOT NULL,
  CertificationName VARCHAR(45) NOT NULL,
  CertificationLevel INT NULL,
  PRIMARY KEY (CertificationID)
  );
  
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Certifications.csv"
INTO TABLE Certifications
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- -----------------------------------------------------
-- Table `EmployeeCertifications`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Employee_Certifications (
  EmployeeID INT,
  CertificationID INT,
  PRIMARY KEY (EmployeeID, CertificationID),
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
  FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Employee_Certifications.csv"
INTO TABLE Employee_Certifications
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- -----------------------------------------------------
-- Tables `Equipment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Equipment (
  EquipmentID BIGINT NOT NULL,
  EquipmentName VARCHAR(45) NOT NULL,
  PRIMARY KEY (EquipmentID)
  );
  
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Equipment.csv"
INTO TABLE Equipment
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS Tool (
  EquipmentToolID BIGINT NOT NULL,
  EquipmentID BIGINT NOT NULL,
  ToolSpecifics VARCHAR(100) NOT NULL,
  ToolID INT NOT NULL,
  Price DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (EquipmentToolID),
  FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Tool.csv"
INTO TABLE Tool
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS Item (
  EquipToolItemID BIGINT NOT NULL,
  EquipmentToolID BIGINT NOT NULL,
  ItemID INT NOT NULL,
  ItemInfo VARCHAR(100) NOT NULL,
  PRIMARY KEY (EquipToolItemID), 
  CONSTRAINT FK_EquipmentToolID FOREIGN KEY (EquipmentToolID) REFERENCES Tool(EquipmentToolID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Item.csv"
INTO TABLE Item
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS CertificationTools (
  CertificationID INT,
  EquipmentToolID BIGINT NOT NULL,
  PRIMARY KEY (CertificationID, EquipmentToolID),
  FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID),
  FOREIGN KEY (EquipmentToolID) REFERENCES Tool(EquipmentToolID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/CertificationTools.csv"
INTO TABLE CertificationTools
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS ToolBox (
  ToolBoxJobID INT NOT NULL,
  ToolBoxID INT NOT NULL,
  JobID INT,
  PRIMARY KEY (ToolBoxJobID),
  FOREIGN KEY (JobID) REFERENCES JobType (JobID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ToolBox.csv"
INTO TABLE ToolBox
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

  CREATE TABLE IF NOT EXISTS TempToolBoxTools (
  ToolBoxJobID INT NOT NULL,
  EquipToolItemID BIGINT NOT NULL
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ToolBoxTools.csv"
INTO TABLE TempToolBoxTools
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS ToolBoxTools (
  EquipToolItemID BIGINT NOT NULL,
  ToolBoxJobID INT NOT NULL,
  PRIMARY KEY (EquipToolItemID, ToolBoxJobID),
  FOREIGN KEY (EquipToolItemID) REFERENCES Item(EquipToolItemID),
  FOREIGN KEY (ToolBoxJobID)  REFERENCES ToolBox(ToolBoxJobID)
  );
  
INSERT INTO ToolBoxTools (EquipToolItemID, ToolBoxJobID)
SELECT 
  CAST(EquipToolItemID AS SIGNED),
  CAST(ToolBoxJobID AS SIGNED)
FROM TempToolBoxTools;


-- Verify Data Import
SELECT 
  tbt.ToolBoxJobID,
  tb.ToolBoxID,
  tb.JobID,
  i.EquipToolItemID,
  i.ItemID,
  i.ItemInfo
FROM 
  ToolBoxTools tbt
JOIN 
  ToolBox tb ON tbt.ToolBoxJobID = tb.ToolBoxJobID
JOIN 
  Item i ON tbt.EquipToolItemID = i.EquipToolItemID
  LIMIT 20;


  CREATE TABLE IF NOT EXISTS TempEmployeeToolBox (
  ToolBoxJobID INT NOT NULL,
  EmployeeID INT
  );
  
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/EmployeeToolBox.csv"
INTO TABLE TempEmployeeToolBox
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS EmployeeToolBox (
  ToolBoxJobID INT,
  EmployeeID INT,
  PRIMARY KEY (ToolBoxJobID, EmployeeID),
  FOREIGN KEY (ToolBoxJobID)  REFERENCES ToolBox(ToolBoxJobID),
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/EmployeeToolBox.csv"
INTO TABLE EmployeeToolBox
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

INSERT INTO EmployeeToolBox (ToolBoxJobID, EmployeeID)
SELECT 
  CAST(ToolBoxJobID AS SIGNED),
  CAST(EmployeeID AS SIGNED)
FROM TempEmployeeToolBox;

-- -----------------------------------------------------
-- Table `ToolJobType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ToolJobType (
  JobID INT,
  EquipmentToolID BIGINT NOT NULL,
  FOREIGN KEY (JobID) REFERENCES JobType(JobID),
  FOREIGN KEY (EquipmentToolID) REFERENCES Tool(EquipmentToolID)
  );
  
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ToolJobType.csv"
INTO TABLE ToolJobType
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- -----------------------------------------------------
-- Table `Site`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Site (
  SiteID INT NOT NULL AUTO_INCREMENT,
  Building VARCHAR(40),
  FloorLevel VARCHAR (40),
  Room VARCHAR(40),
  PRIMARY KEY (SiteID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Site.csv"
INTO TABLE Site
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- -----------------------------------------------------
-- Table `Warehouse`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Warehouse (
  WarehouseID BIGINT NOT NULL,
  WarehouseName VARCHAR(45) NOT NULL,
  PRIMARY KEY (WarehouseID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Warehouse.csv"
INTO TABLE Warehouse
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- -----------------------------------------------------
-- Table `ToolRoom`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ToolRoom (
  ToolRoomID BIGINT NOT NULL,
  ToolRoomName VARCHAR(45) NOT NULL,
  PRIMARY KEY (ToolRoomID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ToolRoom.csv"
INTO TABLE ToolRoom
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS ToolRoomTools (
  EquipToolItemID BIGINT,
  ToolRoomID BIGINT,
  PRIMARY KEY (EquipToolItemID, ToolRoomID),
  FOREIGN KEY (EquipToolItemID) REFERENCES Item(EquipToolItemID),
  FOREIGN KEY (ToolRoomID) REFERENCES ToolRoom(ToolRoomID)
  );
  
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ToolRoomTools.csv"
INTO TABLE ToolRoomTools
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS EmployeeTools (
  EmployeeID INT,
  EquipToolItemID BIGINT,
  ToolRoomID BIGINT,
  PRIMARY KEY (EquipToolItemID, ToolRoomID, EmployeeID),
  FOREIGN KEY (EquipToolItemID) REFERENCES Item(EquipToolItemID),
  FOREIGN KEY (ToolRoomID) REFERENCES ToolRoom(ToolRoomID),
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
  );
  
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/EmployeeTools.csv"
INTO TABLE EmployeeTools
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  
  
-- -----------------------------------------------------
-- Table `WorkOrder`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS WorkOrder (
  WorkOrderID INT NOT NULL AUTO_INCREMENT,
  WorkOrderComments VARCHAR(200),
  EmployeeID INT,
  SiteID INT,
  JobID INT,
  PRIMARY KEY (WorkOrderID),
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
  FOREIGN KEY (SiteID) REFERENCES Site(SiteID),
  FOREIGN KEY (JobID) REFERENCES JobType(JobID)
  );
  
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/WorkOrder.csv"
INTO TABLE WorkOrder
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- -----------------------------------------------------
-- Table `Materials`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Materials (
  MaterialID INT NOT NULL AUTO_INCREMENT,
  MaterialName VARCHAR(45),
  JobID INT,
  PRIMARY KEY (MaterialID),
  FOREIGN KEY (JobID) REFERENCES JobType(JobID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Materials.csv"
INTO TABLE Materials
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS MaterialLocations (
  MaterialLocationID BIGINT,
  MaterialID INT,
  Quantity BIGINT,
  WarehouseID BIGINT,
  PRIMARY KEY (MaterialLocationID),
  FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID),
  FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID)
  );
  
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/MaterialLocation.csv"
INTO TABLE MaterialLocations
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS TransactionTypes (
  TransTypeID INT,
  TransType VARCHAR(15),
  PRIMARY KEY (TransTypeID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/TransactionTypes.csv"
INTO TABLE TransactionTypes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

CREATE TABLE IF NOT EXISTS Location (
  LocationID INT,
  WarehouseID BIGINT,
  ToolRoomID BIGINT, 
  ToolBoxJobID INT,
  SiteID INT,
  PRIMARY KEY (LocationID),
  FOREIGN KEY (ToolRoomID) REFERENCES ToolRoom(ToolRoomID),
  FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID),
  FOREIGN KEY (ToolBoxJobID) REFERENCES ToolBox(ToolBoxJobID),
  FOREIGN KEY (SiteID) REFERENCES Site(SiteID)
  );
  
CREATE TABLE IF NOT EXISTS TempLocation (
  LocationID INT,
  WarehouseID BIGINT NULL DEFAULT NULL,
  ToolRoomID BIGINT NULL DEFAULT NULL, 
  ToolBoxJobID INT NULL DEFAULT NULL,
  SiteID INT NULL DEFAULT NULL
);

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Location.csv"
INTO TABLE TempLocation
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(LocationID, @WarehouseID, @ToolRoomID, @ToolBoxJobID, @SiteID)
SET
WarehouseID = CASE @WarehouseID WHEN 0 THEN NULL ELSE @WarehouseID END,
ToolRoomID = CASE @ToolRoomID WHEN 0 THEN NULL ELSE @ToolRoomID END,
ToolBoxJobID = CASE @ToolBoxJobID WHEN 0 THEN NULL ELSE @ToolBoxJobID END,
SiteID = CASE @SiteID WHEN 0 THEN NULL ELSE @SiteID END;

INSERT INTO Location (LocationID, WarehouseID, ToolRoomID, ToolBoxJobID, SiteID)
SELECT 
  CAST(LocationID AS SIGNED),
  CAST(WarehouseID AS SIGNED),
  CAST(ToolRoomID AS SIGNED),
  CAST(ToolBoxJobID AS SIGNED),
  CAST(SiteID AS SIGNED)
FROM TempLocation;

CREATE TABLE IF NOT EXISTS Transactions (
  TransactionID BIGINT NOT NULL,
  EmployeeID INT NOT NULL,
  EquipToolItemID BIGINT,
  MaterialID INT,
  FromLocationID INT,
  ToLocationID INT,
  TransTypeID INT,
  TransactionDate DATETIME,
  WorkOrderID INT,
  PRIMARY KEY (TransactionID),
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
  FOREIGN KEY (EquipToolItemID) REFERENCES Item(EquipToolItemID),
  FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID),
  FOREIGN KEY (FromLocationID) REFERENCES Location(LocationID),
  FOREIGN KEY (ToLocationID) REFERENCES Location(LocationID),
  FOREIGN KEY (TransTypeID) REFERENCES TransactionTypes(TransTypeID),
  FOREIGN KEY (WorkOrderID) REFERENCES WorkOrder(WorkOrderID)
  );

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Transactions.csv"
INTO TABLE Transactions
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  

-- New Table for Clock-in/out
CREATE TABLE IF NOT EXISTS Clock (
ClockID INT AUTO_INCREMENT,
EmployeeID INT NOT NULL,
Clock_In DATETIME NOT NULL,
Clock_Out DATETIME NULL,
PRIMARY KEY (ClockID),
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
