import sqlite3

db_path = "db.db"

def connect_to_database(db_path):
    try:
        conn = sqlite3.connect(db_path)
        print("Database connected successfully.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def get_data(conn, table_name, conditions=None):
    cursor = conn.cursor()
    if conditions:
        cursor.execute(f"SELECT * FROM {table_name} WHERE {conditions}")
    else:
        cursor.execute(f"SELECT * FROM {table_name}")

    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    result = [{columns[i]: row[i] for i in range(len(columns))} for row in rows]
    return result

def check_data_exists(conn, table_name, condition):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM {table_name} WHERE {condition})")
        result = cursor.fetchone()
        return result[0] == 1 if result else False
    except sqlite3.Error as e:
        print(f"Error checking data existence: {e}")
        return False


def insert_data(conn, table_name, values):
    try:
        cursor = conn.cursor()
        print(f"Attempting to insert values: {values}")
        cursor.execute(
            f"INSERT INTO {table_name} (first_name, last_name, email, username, password) VALUES (?, ?, ?, ?, ?)",
            values
        )
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting data into {table_name}: {e}")

    conn.commit()
