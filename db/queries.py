

#!/usr/bin/env python3
from db.connection import get_connection
import json

def create_user(first_name, last_name, username, password, email):
    query = """
    INSERT INTO users(first_name, last_name, username, password_hash, email, points_balance)
    VALUES (%s, %s, %s, %s, %s, 100) RETURNING user_id;
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (first_name, last_name, username, password, email))
            return cursor.fetchone()["user_id"]



def get_user_by_username(username):
   query = """
   SELECT user_id, username, password_hash FROM users WHERE username = %s;
   """
   with get_connection() as conn:
      with conn.cursor() as cursor:
         cursor.execute(query, (username,))
         return cursor.fetchone()


#!/usr/bin/env python3
def get_user_info(username):
   query = """
   SELECT  first_name, last_name, email, points_balance FROM users WHERE username = %s;
   """
   with get_connection() as conn:
      with conn.cursor() as cursor:
         cursor.execute(query, (username,))
         return cursor.fetchone()

def create_post(poster_id, title, description, quantity, points, zipcode, expiration_date, category_name, image_url ):
   query = """
    INSERT INTO posts(poster_id, title, description, quantity, points, zip_code, expiration_date, category_id, images)
    VALUES(%s, %s, %s, %s, %s, %s, %s,
   (SELECT category_id FROM categories WHERE category_name = %s), %s::jsonb
   )
   RETURNING post_id;
   """
   try:
      images_json = json.dumps(image_url)
      with get_connection() as conn:
         with conn.cursor() as cursor:
            cursor.execute(query, (poster_id,title, description, quantity, points, zipcode, expiration_date, category_name, images_json))
            return cursor.fetchone()["post_id"]
   except Exception as ex:
        print(f"Error in create_post: {str(ex)}")
        raise

def get_all_posts():
   query = """
    SELECT post_id, title, description, quantity, points, zipcode, expiration_date, image_url
    FROM posts;
   """
   with get_connection() as conn:
      with conn.cursor as cursor:
         cursor.execute(query)
         return cursor.fetchall()
def get_post_by_user(user_id):
   query = """SELECT post_id, title, description, quantity, points, zipcode, expiration_date, image_url
   FROM posts WHERE user_id = %;
   """
   with get_connection() as conn:
      with conn.cursor as cursor:
         cursor.execute(query)
         return cursor.fetchall()
      
def reset_points_balance():
    query = """
    UPDATE users
    SET points_balance = 100;
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()  # Commit the changes to the database
            print("All users' points_balance have been reset to 100.")

def get_all_items():
    query = """
    SELECT 
        item_id, trader_id, item_name, description, image_path, points_value,
        category_id, date_listed, is_featured, views_count
    FROM items;
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
