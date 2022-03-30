import sqlite3
conn=sqlite3.connect('test.db')

conn.execute('''
        CREATE TABLE COMPANY (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        NAME   VARCHAR(50)        TEXT    NOT NULL,
        AGE    VARCHAR(2)        INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL)
            ''')
conn.close()   # Close the connection
