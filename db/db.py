import sqlite3
import os
from db import db_path  # Ensure this path is defined in db.py
db_path = "db.db"

def table_exists(conn, table_name):
    """Check if a specific table exists in the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone() is not None

def create_database():
    # Check if the database file exists or create it if it doesn’t
    conn = sqlite3.connect(db_path)
    
    # Check if the "user" table exists
    if not os.path.exists(db_path):
        cursor = conn.cursor()
        
        # Create the "user" table if it doesn't exist
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close
        
    elif not table_exists(conn, "user"):
        cursor = conn.cursor()
        
        cursor.execute(
            """
            CREATE TABLE user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
               
            )
             
                """
    
        )
        conn.commit
        conn.close