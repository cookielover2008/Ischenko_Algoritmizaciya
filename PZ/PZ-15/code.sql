CREATE TABLE Enterprises (
    Enterprise_Code INT PRIMARY KEY,  -- Enterprise code (unique identifier)
    Enterprise_Name VARCHAR(255) NOT NULL,  -- Name of the enterprise
    Physical_Address VARCHAR(255),  -- Physical address
    Branches INT,  -- Number of branches
    Total_Personnel INT,  -- Total number of employees
    Total_Equipment_Value DECIMAL(15, 2),  -- Total value of equipment (with two decimal places)
    Production_Volume DECIMAL(15, 2),  -- Volume of production (with two decimal places)
    Registration_Date DATE  -- Date of registration
);
