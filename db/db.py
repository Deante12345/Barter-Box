import psycopg2
import config

# Set up connection using imported credentials
connection = psycopg2.connect(
    host=config.DB_HOST,
    port=config.DB_PORT,
    dbname=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASSWORD
)

#database connection
cursor = connection.cursor()


#table creation
create_queries = [
"""
CREATE TABLE IF NOT EXISTS users(
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  points_balance INT DEFAULT 0,
  date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""",
"""
CREATE TABLE IF NOT EXISTS items(
  item_id SERIAL PRIMARY KEY,
  trader_id INT REFERENCES users(user_id) ON DELETE CASCADE,
  item_name VARCHAR(255),
  description TEXT NOT NULL,
  image_path TEXT NOT NULL,
  points_value INT NOT NULL,
  category VARCHAR(255) NOT NULL,
  date_listed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  is_featured BOOLEAN NOT NULL,
  views_count INT NOT NULL
);
""",
"""
CREATE TABLE IF NOT EXISTS transactions(
  transaction_id SERIAL PRIMARY KEY,
  sender_id INT REFERENCES users(user_id) ON DELETE CASCADE,
  receiver_id INT REFERENCES users(user_id) ON DELETE CASCADE,
  item_id INT REFERENCES items(item_id) ON DELETE CASCADE,
  points_transferred INT NOT NULL,
  date_of_transaction TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status VARCHAR(50) NOT NULL
);
"""
]
#execute the queries
try:
    for query in create_queries:
        cursor.execute(query)
    connection.commit()
    print("Tables create successfully")
except Exception as e:
    print(f"error creating tables: {e}")
    connection.rollback()
finally:
    #close the connection and cursor
    cursor.close()
    connection.close()
