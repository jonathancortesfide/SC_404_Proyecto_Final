
-- Optional: create the user/schema (requires DBA)
-- CREATE USER ProyectoHotel IDENTIFIED BY "Fidelitas1234";
-- GRANT CONNECT, RESOURCE, CREATE TABLE, CREATE VIEW, CREATE SEQUENCE, CREATE TRIGGER, CREATE PROCEDURE TO ProyectoHotel;

ALTER SESSION SET CURRENT_SCHEMA = ProyectoHotel;

-- ============================================================================
-- Drop existing objects (safe-drop pattern)
-- ============================================================================
BEGIN EXECUTE IMMEDIATE 'DROP VIEW ViewRoomsByHotel';        EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP VIEW RoomByCategoryStatus';    EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP VIEW ViewDetailedRoomReservation'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
-- (ViewDetailedBedReservation referenced non-existent BedReservation table in source; intentionally omitted)

BEGIN EXECUTE IMMEDIATE 'DROP TRIGGER TG_GN_AuditActivity';      EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -4080 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TRIGGER TG_GN_AuditRoomStatus';    EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -4080 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TRIGGER TG_GN_AuditSupplyMovement';EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -4080 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE AuditActivity CASCADE CONSTRAINTS';    EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE AuditRoomStatus CASCADE CONSTRAINTS';  EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE AuditSupplyMovement CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
-- Drop child tables first to avoid FK violations
BEGIN EXECUTE IMMEDIATE 'DROP TABLE ActivityReservation CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE RoomStatus CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE Room CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE Activity CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE Supply CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE Supplier CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE Bed CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE BedCategory CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE ActivityCategory CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE RoomCategory CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE Employee CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE Hotel CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE EmployeeRole CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE Costumer CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE Person CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE StatusCatalog CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE UserMapping CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE UserRole CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;

BEGIN EXECUTE IMMEDIATE 'DROP TABLE RoomReservation CASCADE CONSTRAINTS';    EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;

BEGIN EXECUTE IMMEDIATE 'DROP TABLE AuditActivity CASCADE CONSTRAINTS';    EXCEPTION WHEN OTHERS THEN IF SQLCODE <> -942 THEN RAISE; END IF; END;

BEGIN EXECUTE IMMEDIATE 'DROP TABLE UserRole CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE <> -942 THEN RAISE; END IF;
END;
/

BEGIN EXECUTE IMMEDIATE 'DROP TABLE RoomReservation CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE <> -942 THEN RAISE; END IF;
END;
/
INSERT INTO room VALU
-- ============================================================================
-- Tables (Oracle)
-- ============================================================================

-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025      
-- Description:  Insert a new Activity reservation assoaciated to the customer
-- Materia: Fundamentos de bases de datos relacionales        
-- Version: 1.0.0      
-- REF: 00      
-- HISTORY:      
-- ============================================================================      
CREATE TABLE UserRole (
    UserRoleID NUMBER(10) GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    Name       VARCHAR2(100) NOT NULL,
    Description VARCHAR2(300)
);
/
-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025      
-- Description:  Insert a new room, bed or activity category according to a param
-- Materia: Fundamentos de bases de datos relacionales        
-- Version: 1.0.0      
-- REF: 00      
-- HISTORY:      
-- ============================================================================      
CREATE TABLE UserMapping (
    UserId   NUMBER(10) GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    RoleId   NUMBER(10) NOT NULL,
    Username VARCHAR2(50) UNIQUE NOT NULL,
    CONSTRAINT FK_UserMapping_Role FOREIGN KEY (RoleId) REFERENCES UserRole(UserRoleID)
);
/
-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025       
-- Description:  Insert a Status to the catalog (Able to be used on Rooms,  Beds and Activities)     
-- Materia: Fundamentos de bases de datos relacionales        
-- Version: 1.0.0      
-- REF: 00      
-- HISTORY:      
-- ============================================================================  
CREATE TABLE StatusCatalog (
    StatusId   NUMBER(10) GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    Status     VARCHAR2(100) NOT NULL,
    Description VARCHAR2(300)
);
/
-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025         
-- Description:  Get the list of employees by an Hostal Id      
-- Materia: Fundamentos de bases de datos relacionales        
-- Version: 1.0.0      
-- REF: 00      
-- HISTORY:      
-- ============================================================================  
CREATE TABLE Person (
    Id           NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    Name         VARCHAR2(100),
    PhoneNumber  VARCHAR2(20),
    Email        VARCHAR2(100),
    Address      VARCHAR2(255),
    BirthDate    DATE
);
/
-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025          
-- Description:  Insert a new supplier on the supplier list      
-- Materia: Fundamentos de bases de datos relacionales        
-- Version: 1.0.0      
-- REF: 00      
-- HISTORY:      
-- ============================================================================  
CREATE TABLE Costumer (
    Id               NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    PersonId         NUMBER,
    ReservationCount NUMBER,
    CONSTRAINT FK_Costumer_Person FOREIGN KEY (PersonId) REFERENCES Person(Id)
);
/
-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025     
-- Description:  SP para la inserci�n de Hostales  
-- Materia: Fundamentos de bases de datos relacionales        
-- Version: 1.0.0      
-- REF: 00      
-- HISTORY:      
-- ============================================================================  
CREATE TABLE EmployeeRole (
    Id          NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    Name        VARCHAR2(50),
    Description VARCHAR2(255)
);
/
-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025     
-- Description:  SP para consutar la disponibilidad de una habitaci�n
-- Materia: Fundamentos de bases de datos relacionales        
-- Version: 1.0.0      
-- REF: 00      
-- HISTORY:      
-- ============================================================================  
CREATE TABLE Hotel (
    Id          NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    Name        VARCHAR2(100),
    Description VARCHAR2(255)
);
/
-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025    
-- Description:  SP para la inserci�n de Customers  
-- Materia: Fundamentos de bases de datos relacionales        
-- Version: 1.0.0      
-- REF: 00      
-- HISTORY:      
-- ============================================================================  
CREATE TABLE Employee (
    Id        NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    HotelId   NUMBER,
    PersonId  NUMBER,
    RoleId    NUMBER,
    StartDate DATE,
    Salary    NUMBER(10,2),
    CONSTRAINT FK_Employee_Hotel       FOREIGN KEY (HotelId) REFERENCES Hotel(Id),
    CONSTRAINT FK_Employee_Person      FOREIGN KEY (PersonId) REFERENCES Person(Id),
    CONSTRAINT FK_Employee_EmployeeRole FOREIGN KEY (RoleId) REFERENCES EmployeeRole(Id)
);
/
-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025    
-- Description:  SP para consutar todos los Customers ordenados por su nombre alfabeticamente
-- Materia: Fundamentos de bases de datos relacionales        
-- Version: 1.0.0      
-- REF: 00      
-- HISTORY:      
-- ============================================================================  
CREATE TABLE RoomCategory (
    Id          NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    Category    VARCHAR2(50),
    Description VARCHAR2(255)
);
/
-- ============================================================================
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025    
-- Description: Retrieves all activities for a specific hostel 
-- Materia: Fundamentos de bases de datos relacionales 
-- Version: 1.0.0
-- REF: 00      
-- HISTORY:
-- ============================================================================  
CREATE TABLE Room (
    Id             NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    HotelId        NUMBER,
    RoomCategoryId NUMBER,
    BedsQty        NUMBER,
    Price          NUMBER(10,2),
    CONSTRAINT FK_Room_Hotel        FOREIGN KEY (HotelId) REFERENCES Hotel(Id),
    CONSTRAINT FK_Room_RoomCategory FOREIGN KEY (RoomCategoryId) REFERENCES RoomCategory(Id)
);
/
-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025     
-- Description: Returns the count of suppliers, optionally filtered by hostel 
-- Materia: Fundamentos de bases de datos relacionales 
-- Version: 1.0.0
-- REF: 00      
-- HISTORY:      
-- ============================================================================  
CREATE TABLE RoomStatus (
    Id       NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    RoomId   NUMBER,
    StatusId NUMBER,
    "Comment" VARCHAR2(255),
    CONSTRAINT FK_RoomStatus_Room          FOREIGN KEY (RoomId) REFERENCES Room(Id),
    CONSTRAINT FK_RoomStatus_StatusCatalog FOREIGN KEY (StatusId) REFERENCES StatusCatalog(StatusId)
);
/
-- ============================================================================      
-- Author: Elias Viquez     
-- Create date:  4 Julio 2025       
-- Description: Returns count of reserved and vacant rooms for a specific hostel  
-- Materia: Fundamentos de bases de datos relacionales 
-- Version: 1.0.0
-- REF: 00      
-- HISTORY:      
-- ============================================================================  
CREATE TABLE RoomReservation (
    Id         NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    RoomId     NUMBER,
    CostumerId NUMBER,
    CheckInDate DATE,
    CheckOutDate DATE,
    Price      NUMBER(10,2),
    COMMENTS  VARCHAR2(255),
    CONSTRAINT FK_RoomReservation_Room     FOREIGN KEY (RoomId) REFERENCES Room(Id),
    CONSTRAINT FK_RoomReservation_Costumer FOREIGN KEY (CostumerId) REFERENCES Costumer(Id)
);
/
--View #1: View to check the existing room per each Hostal
CREATE TABLE BedCategory (
    Id          NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    Category    VARCHAR2(50),
    Description VARCHAR2(255)
);
/
--=======================================================================
-- Author: Elias Viquez Segura
-- Creation Date:  05/17/2025
-- Version: 1.0.0
-- REF: 0
-- HISTORY:
--=======================================================================
CREATE TABLE Bed (
    Id           NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    RoomId       NUMBER,
    BedCategoryId NUMBER,
    "Comment"    VARCHAR2(255),
    CONSTRAINT FK_Bed_Room        FOREIGN KEY (RoomId) REFERENCES Room(Id),
    CONSTRAINT FK_Bed_BedCategory FOREIGN KEY (BedCategoryId) REFERENCES BedCategory(Id)
);
/
--SELECT * FROM ViewRoomsByHostal
CREATE TABLE ActivityCategory (
    Id          NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    Name        VARCHAR2(50),
    Description VARCHAR2(255)
);
/
--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- View 2: Shows rooms with their category and status
CREATE TABLE Activity (
    Id                 NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    HotelId            NUMBER,
    ActivityCategoryId NUMBER,
    Price              NUMBER(10,2),
    CONSTRAINT FK_Activity_Hotel            FOREIGN KEY (HotelId) REFERENCES Hotel(Id),
    CONSTRAINT FK_Activity_ActivityCategory FOREIGN KEY (ActivityCategoryId) REFERENCES ActivityCategory(Id)
);
/
--=======================================================================
-- Author: Elias Viquez Segura
-- Creation Date:  05/17/2025
-- Version: 1.0.0
-- REF: 0
-- HISTORY:
--=======================================================================
CREATE TABLE ActivityReservation (
    Id          NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    ActivityId  NUMBER,
    StatusId    NUMBER,
    CostumerId  NUMBER,
    Price       NUMBER(10,2),
    "Comment"   VARCHAR2(255),
    AttenderQty NUMBER,
    CONSTRAINT FK_ActivityReservation_Activity FOREIGN KEY (ActivityId) REFERENCES Activity(Id),
    CONSTRAINT FK_ActivityReservation_Status   FOREIGN KEY (StatusId) REFERENCES StatusCatalog(StatusId),
    CONSTRAINT FK_ActivityReservation_Costumer FOREIGN KEY (CostumerId) REFERENCES Costumer(Id)
);
/
--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- View 3: Shows bookings with customer and room information
CREATE TABLE Supplier (
    Id                NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    HotelId           NUMBER,
    Location          VARCHAR2(100),
    Name              VARCHAR2(100),
    ContactPersonName VARCHAR2(100),
    PhoneNumber       VARCHAR2(20),
    CONSTRAINT FK_Supplier_Hotel FOREIGN KEY (HotelId) REFERENCES Hotel(Id)
);
/
--=======================================================================
-- Author: Elias Viquez Segura
-- Creation Date:  05/17/2025
-- Version: 1.0.0
-- REF: 0
-- HISTORY:
--=======================================================================
CREATE TABLE Supply (
    Id         NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    SupplierId NUMBER,
    SupplyName VARCHAR2(100),
    Qty        NUMBER,
    TotalPrice NUMBER(10,2),
    CONSTRAINT FK_Supply_Supplier FOREIGN KEY (SupplierId) REFERENCES Supplier(Id)
);
/
-- ============================================================================
-- Stored Procedures (Oracle PL/SQL)
-- ============================================================================

-- Insert a new ActivityReservation
--SELECT * FROM ViewDetailedRoomReservation
CREATE OR REPLACE PROCEDURE SP_GN_AddActivityReservation (
    p_ActivityId  NUMBER,
    p_CostumerId  NUMBER DEFAULT NULL,
    p_StatusId    NUMBER DEFAULT NULL,
    p_Price       NUMBER DEFAULT NULL,
    p_Comment     VARCHAR2 DEFAULT NULL,
    p_AttenderQty NUMBER DEFAULT NULL
)
AS
BEGIN
    INSERT INTO ActivityReservation (ActivityId, CostumerId, StatusId, Price, "Comment", AttenderQty)
    VALUES (p_ActivityId, p_CostumerId, p_StatusId, p_Price, p_Comment, p_AttenderQty);
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20010, 'SP_GN_AddActivityReservation failed. '||SQLERRM);
END;
/
-- Insert a new category for ROOM/BED/ACTIVITY
--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- View 4: Shows activities with their category and Hostal
CREATE OR REPLACE PROCEDURE SP_GN_AddNewCategory (
    p_CategoryType VARCHAR2,
    p_CategoryName VARCHAR2 DEFAULT NULL,
    p_Description  VARCHAR2 DEFAULT NULL
)
AS
BEGIN
    IF UPPER(p_CategoryType) = 'ROOM' THEN
        INSERT INTO RoomCategory (Category, Description) VALUES (p_CategoryName, p_Description);
    ELSIF UPPER(p_CategoryType) = 'BED' THEN
        INSERT INTO BedCategory (Category, Description) VALUES (p_CategoryName, p_Description);
    ELSIF UPPER(p_CategoryType) = 'ACTIVITY' THEN
        INSERT INTO ActivityCategory (Name, Description) VALUES (p_CategoryName, p_Description);
    ELSE
        RAISE_APPLICATION_ERROR(-20011, 'Invalid CategoryType: '||p_CategoryType);
    END IF;
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20012, 'SP_GN_AddNewCategory failed. '||SQLERRM);
END;
/
CREATE OR REPLACE PROCEDURE SP_GN_GetActivities (p_cursor OUT SYS_REFCURSOR)
AS
BEGIN
    OPEN p_cursor FOR
        SELECT 
            a.id,
            a.hotelid,
            h.name AS hotel_name,
            a.activitycategoryid,
            ac.name AS activity_category_name,
            a.price
        FROM Activity a
        JOIN Hotel h ON h.id = a.hotelid
        JOIN ActivityCategory ac ON ac.id = a.activitycategoryid
        ORDER BY a.id;
END;

-- Insert a new status into the catalog
--=======================================================================
-- Author: Elias Viquez Segura
-- Creation Date:  05/17/2025
-- Version: 1.0.0
-- REF: 0
-- HISTORY:
--=======================================================================
CREATE OR REPLACE PROCEDURE SP_GN_AddNewStatusToTheCatalog (
    p_Status      VARCHAR2 DEFAULT NULL,
    p_Description VARCHAR2 DEFAULT NULL
)
AS
BEGIN
    INSERT INTO StatusCatalog (Status, Description)
    VALUES (p_Status, p_Description);
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20013, 'SP_GN_AddNewStatusToTheCatalog failed. '||SQLERRM);
END;
/
-- 1. GET all Room Reservations
CREATE OR REPLACE PROCEDURE SP_GN_GetRoomReservations(p_result OUT SYS_REFCURSOR) AS
BEGIN
    OPEN p_result FOR
        SELECT 
            rr.ID,
            rr.ROOMID,
            r.ID AS RoomId,
            r.BEDSQTY AS BedQuantity,
            rr.COSTUMERID,
            p.NAME AS CustomerName,
            rr.CHECKINDATE,
            rr.CHECKOUTDATE,
            rr.PRICE,
            rr.Comments
        FROM RoomReservation rr
        JOIN Room r 
            ON r.ID = rr.ROOMID
        JOIN Costumer c 
            ON c.ID = rr.COSTUMERID
        JOIN Person p 
            ON p.ID = c.PERSONID
        ORDER BY rr.CHECKINDATE DESC;
END;
/



-- 2. GET Room Reservation by ID
CREATE OR REPLACE PROCEDURE SP_GN_GetRoomReservationById(
    p_id IN NUMBER,
    p_result OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_result FOR
        SELECT rr.Id,
               rr.RoomId,
               rr.CostumerId,
               rr.CheckInDate,
               rr.CheckOutDate,
               rr.Price,
               rr.Comments
        FROM RoomReservation rr
        WHERE rr.Id = p_id;
END;
/

-- 3. CREATE Room Reservation
CREATE OR REPLACE PROCEDURE SP_GN_CreateRoomReservation(
    p_RoomId IN NUMBER,
    p_CustomerId IN NUMBER,
    p_CheckInDate IN DATE,
    p_CheckOutDate IN DATE,
    p_Price IN NUMBER,
    p_Comment IN VARCHAR2
) AS
BEGIN
    INSERT INTO RoomReservation (RoomId, CostumerId, CheckInDate, CheckOutDate, Price, Comments)
    VALUES (p_RoomId, p_CustomerId, p_CheckInDate, p_CheckOutDate, p_Price, p_Comment);
END;
/

-- 4. UPDATE Room Reservation
CREATE OR REPLACE PROCEDURE SP_GN_UpdateRoomReservation(
    p_Id IN NUMBER,
    p_RoomId IN NUMBER,
    p_CustomerId IN NUMBER,
    p_CheckInDate IN DATE,
    p_CheckOutDate IN DATE,
    p_Price IN NUMBER,
    p_Comment IN VARCHAR2
) AS
BEGIN
    UPDATE RoomReservation
    SET RoomId = p_RoomId,
        CostumerId = p_CustomerId,
        CheckInDate = p_CheckInDate,
        CheckOutDate = p_CheckOutDate,
        Price = p_Price,
        Comments = p_Comment
    WHERE Id = p_Id;
END;
/

-- 5. DELETE Room Reservation
CREATE OR REPLACE PROCEDURE SP_GN_DeleteRoomReservation(p_id IN NUMBER) AS
BEGIN
    DELETE FROM RoomReservation WHERE Id = p_id;
END;
/

-- Get employees by Hotel Id
--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- View 5: Show Reservations with customer and Bed information
CREATE OR REPLACE PROCEDURE SP_GN_GetEmployeesByHotelId (
    p_HotelId IN NUMBER,
    p_RC OUT SYS_REFCURSOR
)
AS
BEGIN
    OPEN p_RC FOR
        SELECT  e.Id           AS EmployeeId,
                p.Name         AS Name,
                p.Email        AS Email,
                p.PhoneNumber  AS PhoneNumber,
                er.Name        AS RoleName,
                e.StartDate,
                e.Salary
          FROM  Employee e
          JOIN  Person   p  ON p.Id = e.PersonId
          LEFT JOIN EmployeeRole er ON er.Id = e.RoleId
         WHERE  e.HotelId = p_HotelId;
END;
/
-- Insert a new supplier
--=======================================================================
-- Author: Elias Viquez Segura
-- Creation Date:  05/17/2025
-- Version: 1.0.0
-- REF: 0
-- HISTORY:
--=======================================================================
CREATE OR REPLACE PROCEDURE SP_GN_AddNewSupplier (
    p_HotelId           NUMBER DEFAULT NULL,
    p_Name              VARCHAR2 DEFAULT NULL,
    p_Location          VARCHAR2 DEFAULT NULL,
    p_ContactPersonName VARCHAR2 DEFAULT NULL,
    p_PhoneNumber       VARCHAR2 DEFAULT NULL
)
AS
BEGIN
    INSERT INTO Supplier (HotelId, Name, Location, ContactPersonName, PhoneNumber)
    VALUES (p_HotelId, p_Name, p_Location, p_ContactPersonName, p_PhoneNumber);
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20014, 'SP_GN_AddNewSupplier failed. '||SQLERRM);
END;
/
-- Room CRUD
--SELECT * FROM ViewDetailedBedReservation 
CREATE OR REPLACE PROCEDURE SP_GN_AddRoom (
    p_HotelId        NUMBER,
    p_RoomCategoryId NUMBER,
    p_BedsQty        NUMBER,
    p_Price          NUMBER
)
AS
BEGIN
    INSERT INTO Room (HotelId, RoomCategoryId, BedsQty, Price)
    VALUES (p_HotelId, p_RoomCategoryId, p_BedsQty, p_Price);
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20015, 'SP_GN_AddRoom failed. '||SQLERRM);
END;
/
--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ********************************** TRIGGERS **********************************
-- Trigger #1
CREATE OR REPLACE PROCEDURE SP_GN_UpdateRoom (
    p_RoomId         NUMBER,
    p_HotelId        NUMBER DEFAULT NULL,
    p_RoomCategoryId NUMBER DEFAULT NULL,
    p_BedsQty        NUMBER DEFAULT NULL,
    p_Price          NUMBER DEFAULT NULL
)
AS
BEGIN
    UPDATE Room
       SET HotelId        = NVL(p_HotelId, HotelId),
           RoomCategoryId = NVL(p_RoomCategoryId, RoomCategoryId),
           BedsQty        = NVL(p_BedsQty, BedsQty),
           Price          = NVL(p_Price, Price)
     WHERE Id = p_RoomId;
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20016, 'SP_GN_UpdateRoom failed. '||SQLERRM);
END;
/
--=======================================================================
-- Author: Elias Viquez Segura
-- Creation Date:  05/17/2025
-- Description: Trigger to map all updates and Insertion
-- Version: 1.0.0
-- REF: 0
-- HISTORY:
--=======================================================================
CREATE OR REPLACE PROCEDURE SP_GN_DeleteRoom (p_RoomId NUMBER)
AS
BEGIN
    DELETE FROM Room WHERE Id = p_RoomId;
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20017, 'SP_GN_DeleteRoom failed. '||SQLERRM);
END;
/
-- Activity CRUD
--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
-- Trigger #2
CREATE OR REPLACE PROCEDURE SP_GN_AddActivity (
    p_HotelId            NUMBER,
    p_ActivityCategoryId NUMBER,
    p_Price              NUMBER
)
AS
BEGIN
    INSERT INTO Activity (HotelId, ActivityCategoryId, Price)
    VALUES (p_HotelId, p_ActivityCategoryId, p_Price);
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20018, 'SP_GN_AddActivity failed. '||SQLERRM);
END;
/
--=======================================================================
-- Author: Elias Viquez Segura
-- Creation Date:  09/04/2025
-- Description: Audit room status changing when changed manually
-- Version: 1.0.0
-- REF: 0
-- HISTORY:
--=======================================================================
CREATE OR REPLACE PROCEDURE SP_GN_UpdateActivity (
    p_ActivityId         NUMBER,
    p_HotelId            NUMBER DEFAULT NULL,
    p_ActivityCategoryId NUMBER DEFAULT NULL,
    p_Price              NUMBER DEFAULT NULL
)
AS
BEGIN
    UPDATE Activity
       SET HotelId            = NVL(p_HotelId, HotelId),
           ActivityCategoryId = NVL(p_ActivityCategoryId, ActivityCategoryId),
           Price              = NVL(p_Price, Price)
     WHERE Id = p_ActivityId;
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20019, 'SP_GN_UpdateActivity failed. '||SQLERRM);
END;
/
--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
-- Trigger #3
CREATE OR REPLACE PROCEDURE SP_GN_DeleteActivity (p_ActivityId NUMBER)
AS
BEGIN
    DELETE FROM Activity WHERE Id = p_ActivityId;
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20020, 'SP_GN_DeleteActivity failed. '||SQLERRM);
END;
/
-- Add Hotel (keeping original name FN_GN_AddHostal but targeting HOTEL table)
--=======================================================================
-- Author: Elias Viquez Segura
-- Creation Date:  05/17/2025
-- Description: Trigger to map all Entries and movements of supplies
-- Version: 1.0.0
-- REF: 0
-- HISTORY:
--=======================================================================
CREATE OR REPLACE PROCEDURE FN_GN_AddHotel (
    p_Nombre      VARCHAR2,
    p_Description VARCHAR2
)
AS
BEGIN
    INSERT INTO Hotel (Name, Description) VALUES (p_Nombre, p_Description);
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20021, 'FN_GN_AddHostal failed. '||SQLERRM);
END;
/
CREATE OR REPLACE PROCEDURE FN_GN_UpdateHotel (
    p_HotelId    NUMBER,
    p_Nombre     VARCHAR2,
    p_Description VARCHAR2
)
AS
BEGIN
    UPDATE Hotel
       SET Name = p_Nombre,
           Description = p_Description
     WHERE Id = p_HotelId;
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20022, 'FN_GN_UpdateHotel failed. '||SQLERRM);
END;
/
CREATE OR REPLACE PROCEDURE FN_GN_DeleteHotel (
    p_HotelId NUMBER
)
AS
BEGIN
    DELETE FROM Hotel WHERE Id = p_HotelId;
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20023, 'FN_GN_DeleteHotel failed. '||SQLERRM);
END;

/
-- Get room status (by Room Id)
CREATE OR REPLACE PROCEDURE FN_GN_GetRoomStatus (
    p_RoomId IN NUMBER,
    p_RC OUT SYS_REFCURSOR
)
AS
BEGIN
    OPEN p_RC FOR
        SELECT sc.Status
          FROM RoomStatus rs
          JOIN StatusCatalog sc ON sc.StatusId = rs.StatusId
         WHERE rs.RoomId = p_RoomId;
END;
/
-- Add Employee
CREATE OR REPLACE PROCEDURE SP_GN_AddEmployee (
    p_HotelId  NUMBER,
    p_PersonId NUMBER,
    p_RoleId   NUMBER,
    p_StartDate DATE,
    p_Salary   NUMBER
)
AS
BEGIN
    INSERT INTO Employee (HotelId, PersonId, RoleId, StartDate, Salary)
    VALUES (p_HotelId, p_PersonId, p_RoleId, p_StartDate, p_Salary);
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20030, 'SP_GN_AddEmployee failed. '||SQLERRM);
END;
/

-- Update Employee
CREATE OR REPLACE PROCEDURE SP_GN_UpdateEmployee (
    p_EmployeeId NUMBER,
    p_HotelId    NUMBER DEFAULT NULL,
    p_PersonId   NUMBER DEFAULT NULL,
    p_RoleId     NUMBER DEFAULT NULL,
    p_StartDate  DATE DEFAULT NULL,
    p_Salary     NUMBER DEFAULT NULL
)
AS
BEGIN
    UPDATE Employee
       SET HotelId   = NVL(p_HotelId, HotelId),
           PersonId  = NVL(p_PersonId, PersonId),
           RoleId    = NVL(p_RoleId, RoleId),
           StartDate = NVL(p_StartDate, StartDate),
           Salary    = NVL(p_Salary, Salary)
     WHERE Id = p_EmployeeId;
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20031, 'SP_GN_UpdateEmployee failed. '||SQLERRM);
END;
/

-- Delete Employee
CREATE OR REPLACE PROCEDURE SP_GN_DeleteEmployee (p_EmployeeId NUMBER)
AS
BEGIN
    DELETE FROM Employee WHERE Id = p_EmployeeId;
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20032, 'SP_GN_DeleteEmployee failed. '||SQLERRM);
END;
/

-- Get Employees
CREATE OR REPLACE PROCEDURE SP_GN_GetEmployees (p_cursor OUT SYS_REFCURSOR)
AS
BEGIN
    OPEN p_cursor FOR
        SELECT e.Id, e.HotelId, h.Name AS hotel_name,
               e.PersonId, p.Name AS person_name,
               e.RoleId, r.Name AS role_name,
               e.StartDate, e.Salary
          FROM Employee e
          JOIN Hotel h ON h.Id = e.HotelId
          JOIN Person p ON p.Id = e.PersonId
          JOIN EmployeeRole r ON r.Id = e.RoleId
         ORDER BY e.Id;
END;
/

-- Add Costumer (creates PERSON then COSTUMER row)
CREATE OR REPLACE PROCEDURE SP_GN_GetCustomers(p_cursor OUT SYS_REFCURSOR)
AS
BEGIN
    OPEN p_cursor FOR
        SELECT 
            c.Id,
            c.PersonId,
            p.Name AS person_name,
            c.ReservationCount
        FROM Costumer c
        JOIN Person p ON p.Id = c.PersonId
        ORDER BY c.Id;
END;
/
CREATE OR REPLACE PROCEDURE SP_GN_AddCustomer(
    p_person_id IN NUMBER,
    p_reservation_count IN NUMBER
)
AS
BEGIN
    INSERT INTO Costumer (PersonId, ReservationCount)
    VALUES (p_person_id, p_reservation_count);
    
    COMMIT;
END;
/
CREATE OR REPLACE PROCEDURE SP_GN_UpdateCustomer(
    p_customer_id IN NUMBER,
    p_person_id IN NUMBER,
    p_reservation_count IN NUMBER
)
AS
BEGIN
    UPDATE Costumer
    SET PersonId = p_person_id,
        ReservationCount = p_reservation_count
    WHERE Id = p_customer_id;
    
    COMMIT;
END;
/
CREATE OR REPLACE PROCEDURE SP_GN_DeleteCustomer(
    p_customer_id IN NUMBER
)
AS
BEGIN
    DELETE FROM Costumer
    WHERE Id = p_customer_id;
    
    COMMIT;
END;
/

/
-- ============================================================================
-- Functions (Oracle)
-- ============================================================================

-- Returns all activities for a specific hotel (as ref cursor)
CREATE OR REPLACE FUNCTION fn_GetActivitiesByHostal (p_HotelId IN NUMBER)
RETURN SYS_REFCURSOR
AS
    rc SYS_REFCURSOR;
BEGIN
    OPEN rc FOR
        SELECT  a.Id AS ActivityId,
                a.Price,
                ac.Name AS CategoryName,
                ac.Description AS CategoryDescription
          FROM Activity a
          JOIN ActivityCategory ac ON ac.Id = a.ActivityCategoryId
         WHERE a.HotelId = p_HotelId;
    RETURN rc;
END;
/
-- Returns supplier count (scalar)
CREATE OR REPLACE FUNCTION fn_GetSupplierCount
RETURN NUMBER
AS
    v_Count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_Count FROM Supplier;
    RETURN v_Count;
END;
/
-- Returns room status counts for a hotel (as ref cursor)
CREATE OR REPLACE FUNCTION fn_GetRoomStatusCountByHostal (p_HotelId IN NUMBER)
RETURN SYS_REFCURSOR
AS
    rc SYS_REFCURSOR;
BEGIN
    OPEN rc FOR
        SELECT  sc.Status,
                COUNT(*) AS RoomCount
          FROM Room r
          JOIN RoomStatus rs ON rs.RoomId = r.Id
          JOIN StatusCatalog sc ON sc.StatusId = rs.StatusId
         WHERE r.HotelId = p_HotelId
      GROUP BY sc.Status;
    RETURN rc;
END;
/
-- ============================================================================
-- Views (Oracle)
-- ============================================================================

-- View #1: Rooms per Hotel
CREATE OR REPLACE VIEW ViewRoomsByHotel AS
SELECT  h.Id AS HotelId,
        h.Name AS HotelName,
        r.Id AS RoomId,
        r.RoomCategoryId,
        r.BedsQty,
        r.Price
  FROM  Hotel h
  JOIN  Room  r ON r.HotelId = h.Id
  JOIN  RoomCategory rc ON rc.Id = r.RoomCategoryId;
/
-- View #2: Rooms with category and current status (last status row per room if multiples exist)
CREATE OR REPLACE VIEW RoomByCategoryStatus AS
SELECT  r.Id AS RoomId,
        rc.Category,
        sc.Status
  FROM  Room r
  JOIN  RoomCategory rc ON rc.Id = r.RoomCategoryId
  JOIN  RoomStatus rs ON rs.RoomId = r.Id
  JOIN  StatusCatalog sc ON sc.StatusId = rs.StatusId;
/
-- View #3: Room reservations with customer and room info
CREATE OR REPLACE VIEW ViewDetailedRoomReservation AS
SELECT  rr.Id              AS BookingId,
        p.Name            AS CustomerName,
        r.Id              AS RoomNumber,
        rc.Category       AS RoomType,
        rr.CheckInDate,
        rr.CheckOutDate,
        rr.Price          AS TotalPrice,
        (rr.CheckOutDate - rr.CheckInDate) AS DaysReserved
  FROM  RoomReservation rr
  JOIN  Room r          ON r.Id = rr.RoomId
  JOIN  Costumer c      ON c.Id = rr.CostumerId
  JOIN  Person p        ON p.Id = c.PersonId
  JOIN  RoomCategory rc ON rc.Id = r.RoomCategoryId;
/
-- Note: ViewDetailedBedReservation omitted (no BedReservation table in source).

-- ============================================================================
-- Audit Tables & Triggers (Oracle)
-- ============================================================================

CREATE TABLE AuditActivity (
    AuditId   NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    HotelId   NUMBER,
    ActivityId NUMBER,
    Action    VARCHAR2(30) NOT NULL,
    EventDate DATE DEFAULT SYSDATE,
    "User"    VARCHAR2(50) DEFAULT SYS_CONTEXT('USERENV','SESSION_USER'),
    Detail    VARCHAR2(500)
);
/
CREATE OR REPLACE TRIGGER TG_GN_AuditActivity
AFTER INSERT OR UPDATE ON Activity
FOR EACH ROW
BEGIN
    IF INSERTING THEN
        INSERT INTO AuditActivity (HotelId, ActivityId, Action, Detail)
        VALUES (
            :NEW.HotelId,
            :NEW.Id,
            'INSERT',
            'NEW VALUES: ActivityId='||:NEW.Id||
            ', CategoryId='||:NEW.ActivityCategoryId||
            ', Price='||:NEW.Price||
            ', HotelId='||:NEW.HotelId
        );
    ELSIF UPDATING THEN
        INSERT INTO AuditActivity (HotelId, ActivityId, Action, Detail)
        VALUES (
            :NEW.HotelId,
            :NEW.Id,
            'UPDATE',
            'NEW VALUES: ActivityId='||:NEW.Id||
            ', CategoryId='||:NEW.ActivityCategoryId||
            ', Price='||:NEW.Price||
            ', HotelId='||:NEW.HotelId
        );
    END IF;
END;

/
CREATE TABLE AuditRoomStatus (
    AuditId   NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    RoomId    NUMBER,
    Action    VARCHAR2(30) NOT NULL,
    EventDate DATE DEFAULT SYSDATE,
    "User"    VARCHAR2(50) DEFAULT SYS_CONTEXT('USERENV','SESSION_USER'),
    Detail    VARCHAR2(500)
);
/
CREATE OR REPLACE TRIGGER TG_GN_AuditRoomStatus
AFTER UPDATE ON RoomStatus
FOR EACH ROW
BEGIN
    INSERT INTO AuditRoomStatus (RoomId, Action, Detail)
    VALUES (
        :NEW.RoomId,
        'UPDATE',
        'NEW VALUES: StatusId='||:NEW.StatusId||', Comment='||:NEW."Comment"
    );
END;
/
CREATE TABLE AuditSupplyMovement (
    AuditId   NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    SupplyId  NUMBER,
    Action    VARCHAR2(30) NOT NULL,
    EventDate DATE DEFAULT SYSDATE,
    "User"    VARCHAR2(50) DEFAULT SYS_CONTEXT('USERENV','SESSION_USER'),
    Detail    VARCHAR2(500)
);
/
CREATE OR REPLACE TRIGGER TG_GN_AuditSupplyMovement
AFTER INSERT OR UPDATE ON Supply
FOR EACH ROW
BEGIN
    IF INSERTING THEN
        INSERT INTO AuditSupplyMovement (SupplyId, Action, Detail)
        VALUES (
            :NEW.Id,
            'INSERT',
            'NEW VALUES: SupplierId='||:NEW.SupplierId||
            ', Qty='||:NEW.Qty||
            ', SupplyName='||:NEW.SupplyName||
            ', TotalPrice='||:NEW.TotalPrice
        );
    ELSIF UPDATING THEN
        INSERT INTO AuditSupplyMovement (SupplyId, Action, Detail)
        VALUES (
            :NEW.Id,
            'UPDATE',
            'NEW VALUES: SupplierId='||:NEW.SupplierId||
            ', Qty='||:NEW.Qty||
            ', SupplyName='||:NEW.SupplyName||
            ', TotalPrice='||:NEW.TotalPrice
        );
    END IF;
END;
/

