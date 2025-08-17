import mysql.connector
import pymysql

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="DeVry123",
            database="mydb",
        )
    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection successful!")
        except pymysql.MySQLError as e:
            print(f"Error connecting to database: {e}")
    def search(self, query, params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"Error executing search: {e}")
            return None

    def update(self, query, params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                print("Update successful!")
        except pymysql.MySQLError as e:
            print(f"Error executing update: {e}")
            self.connection.rollback()
    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")


#C:\Users\Jimdav1977\Desktop\DeVry Scool\CEIS400 Engineering\Python SQL merge