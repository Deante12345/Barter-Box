import sqlite3
import os
from db import db_path


def table_exists(conn, table_name):
    cursor = conn.cursor()
    cursor.excute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", {table_name})
    return cursor.fetchone() is not None


def create_database():
    
    conn = sqlite3.connect(db_path)
    
    if not os.path.exists(db_path):
        cursor = conn.cursor()
        
        cursor.execute(
        
        """
        CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
        )
        
        """
    )
    
    conn.commit()
    conn.close()
    
elif not table_exists(conn, "user"):
    cursor = conn.cursor()
    
    cursor.execute(
    """
     CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
        )
        
        """
    )