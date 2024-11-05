import sqlite3

def connect_to_database(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def get_data(conn, table_name, conditions =None):
    cursor = conn.cursor()
    if conditions:
        cursor.execute(f"SELECT * FROM
                       {table_name} WHERE
                       {conditions}")
        
    else: 
        cursor.excute(f"SELECT * FROM {table_name}")
        
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result = [{columns[i]:row[i]} for i in range(len(columns)) for row in rows]
        return result
    
    def check_data_exists(conn, table_name, condition):
        cursor = conn.cursor()
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM {table_name} WHERE {condition})")
        return cursor.fetchone()[0] == 1
    
    
        def insert_data(conn, table_name, values):
            cursor = conn.curssor()
            cursor.execute(
                f"INSERT INTO {table_name} (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
                values
            )
            conn.commit()