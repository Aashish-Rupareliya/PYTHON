# user.py
from db_connection import get_db_connection
import hashlib

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.role = role

    def register(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                (self.username, self.password, self.role)
            )
            conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def login(username, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute(
            "SELECT role FROM users WHERE username=%s AND password=%s",
            (username, hashed_password)
        )
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
