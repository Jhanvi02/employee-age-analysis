import sqlite3

def setup_database():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.executescript("""
    DROP TABLE IF EXISTS DEPARTMENT;
    DROP TABLE IF EXISTS EMPLOYEE;
    DROP TABLE IF EXISTS PAYMENTS;

    CREATE TABLE DEPARTMENT (
        DEPARTMENT_ID INTEGER PRIMARY KEY,
        DEPARTMENT_NAME TEXT
    );

    CREATE TABLE EMPLOYEE (
        EMP_ID INTEGER PRIMARY KEY,
        FIRST_NAME TEXT,
        LAST_NAME TEXT,
        DOB DATE,
        GENDER TEXT,
        DEPARTMENT INTEGER,
        FOREIGN KEY (DEPARTMENT) REFERENCES DEPARTMENT(DEPARTMENT_ID)
    );

    CREATE TABLE PAYMENTS (
        PAYMENT_ID INTEGER PRIMARY KEY,
        EMP_ID INTEGER,
        AMOUNT REAL,
        PAYMENT_TIME TEXT,
        FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE(EMP_ID)
    );

    INSERT INTO DEPARTMENT VALUES
        (1, 'HR'), (2, 'Finance'), (3, 'Engineering'),
        (4, 'Sales'), (5, 'Marketing'), (6, 'IT');

    INSERT INTO EMPLOYEE VALUES
        (1, 'John', 'Williams', '1980-05-15', 'Male', 3),
        (2, 'Sarah', 'Johnson', '1990-07-20', 'Female', 2),
        (3, 'Michael', 'Smith', '1985-02-10', 'Male', 3),
        (4, 'Emily', 'Brown', '1992-11-30', 'Female', 4),
        (5, 'David', 'Jones', '1988-09-05', 'Male', 5),
        (6, 'Olivia', 'Davis', '1995-04-12', 'Female', 1),
        (7, 'James', 'Wilson', '1983-03-25', 'Male', 6),
        (8, 'Sophia', 'Anderson', '1991-08-17', 'Female', 4),
        (9, 'Liam', 'Miller', '1979-12-01', 'Male', NULL),
        (10, 'Emma', 'Taylor', '1993-06-28', 'Female', 5);

    INSERT INTO PAYMENTS VALUES
        (1, 2, 65784.00, '2025-01-01 13:44:12.824'),
        (2, 4, 62736.00, '2025-01-06 18:36:37.892'),
        (3, 1, 69437.00, '2025-01-01 10:19:21.563'),
        (4, 3, 67183.00, '2025-01-02 17:21:57.341'),
        (5, 2, 66273.00, '2025-02-01 11:49:15.764'),
        (6, 5, 71475.00, '2025-01-01 07:24:14.453'),
        (7, 1, 70837.00, '2025-02-03 19:11:31.553'),
        (8, NULL, 69628.00, '2025-01-02 10:41:15.113'),
        (9, 4, 71876.00, '2025-02-01 12:16:47.807'),
        (10, 3, 70098.00, '2025-02-03 10:11:17.341'),
        (11, 6, 67827.00, '2025-02-02 19:21:27.753'),
        (12, 5, 69871.00, '2025-02-05 17:54:17.453'),
        (13, NULL, 72984.00, '2025-03-05 09:37:35.974'),
        (14, NULL, 67982.00, '2025-03-01 06:09:51.983'),
        (15, NULL, 70198.00, '2025-03-02 10:34:35.753'),
        (16, 4, 74998.00, '2025-03-02 09:27:26.162');
    """)
    conn.commit()
    conn.close()