create database TestDB
GO
use TestDB
GO

CREATE TABLE EMP(
EMP_ID int NOT NULL Primary key,
FIRST_NAME varchar(20), 
LAST_NAME varchar(20), 
AGE INT, 
SEX varchar(5), 
EMAIL_ID varchar(50),
PHONE_NO varchar(15), 
DEPARTMENT_ID INT, 
DESIGNATION_ID INT,
MANAGER_ID INT,
[LEVEL] INT,
INCOME float,
COMMISSION float,
FOREIGN KEY(DEPARTMENT_ID) REFERENCES DEPARTMENT(DEPARTMENT_ID),
FOREIGN KEY(DESIGNATION_ID) REFERENCES DESIGNATION(DESIGNATION_ID)
)
GO

INSERT INTO EMP(EMP_ID, FIRST_NAME, LAST_NAME, AGE, SEX, EMAIL_ID, PHONE_NO, DEPARTMENT_ID,DESIGNATION_ID, MANAGER_ID,[LEVEL], INCOME,COMMISSION) 
VALUES
(1, 'John', 'Doe', 30, 'M', 'john.doe@example.com', '1234567890', 2, 75000.00,11250.00),
(2, 'Jane', 'Smith', 28, 'F', 'jane.smith@example.com', '1235557890', 'Data Analyst', 1, 68000.00,13600.00),
(3, 'Michael', 'Johnson', 35, 'M', 'michael.johnson@example.com', '1236667890', 'Project Manager', 3, 95000.00,9500.00),
(4, 'Emily', 'Williams', 40, 'F', 'emily.williams@example.com', '1237777890', 'HR Manager', 3, 80000.00,8000.00),
(5, 'David', 'Brown', 45, 'M', 'david.brown@example.com', '1238887890', 'CTO', 4, 120000.00, 6000.00),
(6, 'Sarah', 'Davis', 32, 'F', 'sarah.davis@example.com', '1239997890', 'UX Designer', 2, 72000.00, 10800.00),
(7, 'James', 'Miller', 50, 'M', 'james.miller@example.com', '1230007890', 'CEO', 1, 150000.00, 30000.00),
(8, 'Linda', 'Wilson', 26, 'F', 'linda.wilson@example.com', '1231117890', 'Marketing Specialist', 1, 65000.00, 13000.00),
(9, 'Robert', 'Moore', 33, 'M', 'robert.moore@example.com', '1232227890', 'Sales Executive', 2, 70000.00, 10500.00),
(10, 'Olivia', 'Taylor', 29, 'F', 'olivia.taylor@example.com', '1233337890', 'Financial Analyst', 1, 68000.00, 13600.00)
GO

INSERT INTO EMP (EMP_ID, FIRST_NAME, LAST_NAME, AGE, SEX, EMAIL_ID, PHONE_NO, DEPARTMENT_ID, DESIGNATION_ID, MANAGER_ID, [LEVEL], INCOME, COMMISSION)
VALUES 
(1, 'John', 'Doe', 30, 'Male', 'john.doe@example.com', '123-456-7890', 1, 2, NULL, 4, 60000.00, 3000.00)
GO
(2, 'Jane', 'Smith', 28, 'Female', 'jane.smith@example.com', '123-456-7891', 2, 3, 1, 3, 50000.00, 4000.00),
(3, 'Alice', 'Johnson', 35, 'Female', 'alice.johnson@example.com', '123-456-7892', 3, 4, 2, 1, 45000.00, 3500.00),
(4, 'Bob', 'Brown', 40, 'Male', 'bob.brown@example.com', '123-456-7893', 4, 5, 3, 2, 70000.00, 6000.00),
(5, 'Charlie', 'Davis', 25, 'Male', 'charlie.davis@example.com', '123-456-7894', 5, 6, 4, 1, 40000.00, 3000.00);



select * from emp
GO
drop procedure sp_insert_data
-- STORED PROCEDURE FOR @SERT DATA @ THE TABLE EMP.
CREATE PROCEDURE sp_insert_data(
    @emp_id INT,
    @fname VARCHAR(20),
    @lname VARCHAR(20),
    @age INT,
    @sex VARCHAR(1),
	@emailid varchar(40),
	@phoneno varchar(15),
	@departmentID INT,
	@designationID INT,
	@managerID INT,
	@level int,
    @Income FLOAT,
	@commission float
)
AS
BEGIN
    INSERT INTO emp(EMP_ID, FIRST_NAME, LAST_NAME, AGE, SEX, EMAIL_ID, PHONE_NO, DEPARTMENT_ID, DESIGNATION_ID, MANAGER_ID,[LEVEL] ,INCOME, COMMISSION) 
    VALUES (@emp_id, @fname, @lname, @age, @sex, @emailid, @phoneno, @departmentID, @designationID, @managerID,@level,@Income,@commission)
END 
GO
drop procedure sp_update_data
-- STORED PROCEDURE FOR UPDATE DATA @ THE TABLE EMP
CREATE PROCEDURE sp_update_data(
    @emp_id INT,
    @fname VARCHAR(20),
    @lname VARCHAR(20),
    @age INT,
    @sex VARCHAR(1),
	@emailid varchar(40),
	@phoneno varchar(15),
	@departmentID INT,
	@designationID INT,
	@managerID INT,
	@level int,
    @Income FLOAT,
	@commission float
)
AS
BEGIN
     UPDATE emp
     SET First_name=@fname , last_name=@lname , age=@age , sex=@sex , Email_id=@emailid,Phone_no=@phoneno, DEPARTMENT_ID=@departmentID,DESIGNATION_ID=@designationID, MANAGER_ID=@managerID, [LEVEL]=@level,Income=@Income, Commission=@commission
     WHERE emp_id=@emp_id
END
GO

-- STORED PROCEDURE FOR DELETE RECORD FOR TABLE EMP
CREATE PROCEDURE sp_delete_data(
    @emp_id INT
)
AS
BEGIN
		DELETE FROM EMP WHERE emp_id=@emp_id
END
GO

-- STORED PROCEDURE FOR RETRIEVE ALL RECORDS FROM THE TABLE EMP
CREATE PROCEDURE sp_retrieve_alldata
AS
BEGIN
		SELECT * FROM emp
END
GO

-- STORED PROCEDURE FOR RETRIEVE THE FILTER DATA
CREATE PROCEDURE sp_retrievefilterdata(@id INT)
AS
BEGIN
		SELECT * FROM emp WHERE emp_id=@id
END
GO


-- STORED PROCEDURE FOR RETREIVING MAX(ID) FROM THE TABLE EMP
CREATE PROCEDURE sp_automatic_emp_id
AS
BEGIN
	SELECT MAX(EMP_ID) FROM emp;
END
GO
use TestDB
GO
-- STORED PROCEDURE FOR RETREIVING DATA USING SOME SPECIFIC RANDOM INPUT COLUMN VALUES.
ALTER PROCEDURE sp_data_retrieval 
    @column_name VARCHAR(40), 
    @column_value SQL_VARIANT
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    
    -- Constructing the dynamic SQL string
    SET @sql = 'SELECT * FROM emp WHERE ' + QUOTENAME(@column_name) + ' = @column_value';

    -- Execute the dynamic SQL with the proper parameter binding
    EXEC sp_executesql @sql, 
        N'@column_value SQL_VARIANT', 
        @column_value;
END
GO

exec sp_data_retrieval 'last_name','Doe'
GO

USE TestDB
GO
CREATE TABLE Designation(
DESIGNATION_ID INT PRIMARY KEY,
DESIGNATION VARCHAR(40) NOT NULL
)
GO

CREATE TABLE Department(
DEPARTMENT_ID INT PRIMARY KEY,
DEPARTMENT VARCHAR(40) NOT NULL
)
GO

CREATE TABLE Dep_Desig(
DEPARTMENT_ID INT NOT NULL,
DESIGNATION_ID INT NOT NULL,
PRIMARY KEY (DEPARTMENT_ID,DESIGNATION_ID),
FOREIGN KEY (DEPARTMENT_ID) REFERENCES Department(DEPARTMENT_ID),
FOREIGN KEY (DESIGNATION_ID) REFERENCES Designation(DESIGNATION_ID)
)
GO

INSERT INTO DEPARTMENT
VALUES
(1, 'Executive'),
(2, 'Engineering'),
(3, 'Product Management'),
(4, 'Marketing'),
(5, 'Project Management'),
(6, 'Business Analysis'),
(7, 'HR'),
(8, 'Sales'),
(9, 'Finance'),
(10, 'IT Support'),
(11, 'Administration'),
(12, 'Networking & Database')
go

INSERT INTO DESIGNATION VALUES
(1, 'CEO (Chief Executive Officer)'),
(2, 'CTO (Chief Technology Officer)'),
(3, 'CIO (Chief Information Officer)'),
(4, 'COO (Chief Operating Officer)'),
(5, 'CFO (Chief Financial Officer)'),
(6, 'VP of Engineering'),
(7, 'Director of Engineering'),
(8, 'Software Architect'),
(9, 'Engineering Manager'),
(10, 'Technical Lead'),
(11, 'Senior Software Engineer'),
(12, 'Software Engineer'),
(13, 'Junior Software Developer'),
(14, 'DevOps Engineer'),
(15, 'Systems Administrator'),
(16, 'VP of Product Management'),
(17, 'Director of Product Management'),
(18, 'VP of Marketing'),
(19, 'Marketing Manager'),
(20, 'Marketing Coordinator'),
(21, 'Digital Marketing Specialist'),
(22, 'Project Manager'),
(23, 'Business Analyst'),
(24, 'HR Manager'),
(25, 'HR Coordinator'),
(26, 'Recruiter'),
(27, 'Payroll Coordinator'),
(28, 'HR Specialist'),
(29, 'Sales Manager'),
(30, 'Sales Representative'),
(31, 'Finance Manager'),
(32, 'Accountant'),
(33, 'IT Support Specialist'),
(34, 'Receptionist'),
(35, 'Database Administrator'),
(36, 'Network Administrator')
GO
SELECT * FROM Dep_Desig
INSERT INTO Dep_Desig
VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(2, 6),
(2, 7),
(2, 8),
(2, 9),
(2, 10),
(2, 11),
(2, 12),
(2, 13),
(2, 14),
(2, 15),
(3, 16),
(3, 17),
(4, 18),
(4, 19),
(4, 20),
(4, 21),
(5, 22),
(6, 23),
(7, 24),
(7, 25),
(7, 26),
(7, 27),
(7, 28),
(8, 29),
(8, 30),
(9, 31),
(9, 32),
(10, 33),
(11, 34),
(12, 35),
(12, 36)
GO
USE TESTDB
GO
