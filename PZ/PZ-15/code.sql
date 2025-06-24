CREATE TABLE IF NOT EXISTS Enterprises (
    Enterprise_Code INT PRIMARY KEY, 
    Enterprise_Name VARCHAR(255) NOT NULL,
    Physical_Address VARCHAR(255),
    Branches INT, 
    Total_Personnel INT, 
    Total_Equipment_Value DECIMAL(15, 2),  
    Production_Volume DECIMAL(15, 2), 
    Registration_Date DATE  
);
