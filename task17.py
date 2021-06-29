#connection for DB:

import sqlite3
try:
   sqlite_Connection = sqlite3.connect('temp.db')
   conn = sqlite_Connection.cursor()
   print("\nDatabase created and connected to SQLite.")
   sqlite_select_Query = "select sqlite_version();"
   conn.execute(sqlite_select_Query)
   record = conn.fetchall()
   print("\nSQLite Database Version is: ", record)
   conn.close()
except sqlite3.Error as error:
   print("\nError while connecting to sqlite", error)
finally:
   if (sqlite_Connection):
       sqlite_Connection.close()
       print("\nThe SQLite connection is closed.")
       
 #Multiple tables:
 	import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES (%s, %s, %s, %s) """

    records_to_insert = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),
                         (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
                         (6, 'Microsoft Surface', 2330, '2019-07-23')]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

#Employee table:

CREATE TABLE `employees`.`tblemployee` (
  `Employee_ID` INT NOT NULL AUTO_INCREMENT,
  `Employee_Name` VARCHAR(45) NOT NULL,
  `Employee_Department_ID` INT NOT NULL,
  `Employee_Grade_ID` INT NOT NULL DEFAULT A,
  `Employee_Salary` INT NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  INDEX `FK_Department_ID_idx` (`Employee_Department_ID` ASC) VISIBLE,
  CONSTRAINT `FK_Department_ID`
    FOREIGN KEY (`Employee_Department_ID`)
    REFERENCES ` employees`.`department` (`Department_ID`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE);