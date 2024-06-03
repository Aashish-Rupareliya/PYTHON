# db_connection.py
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="product_management"
    )
