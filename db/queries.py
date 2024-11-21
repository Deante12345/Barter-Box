#!/usr/bin/env python3
from db.connection import get_connection

def create_user(first_name, last_name, username, password, email):
   query = """
    INSERT INTO users(first_name, last_name, username, password_hash, email)
    VALUES (%s, %s, %s, %s, %s) RETURNING user_id;
   """
   with get_connection() as conn:
       with conn.cursor() as cursor:
           cursor.execute(query, (first_name, last_name, username,
                                  password, email))
           return cursor.fetchone()["user_id"]

def get_user_by_username(username):
   query = """
   SELECT user_id, username, password_hash FROM users WHERE username = %s;
   """
   with get_connection() as conn:
      with conn.cursor() as cursor:
         cursor.execute(query, (username,))
         return cursor.fetchone()
