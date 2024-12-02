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
#"""
#  CREATE TYPE transaction_status AS ENUM ('Pending', 'Completed', 'Failed');
#"""
 #   ,
"""
CREATE TABLE IF NOT EXISTS users(
  user_id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  username VARCHAR(255) UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  points_balance INT DEFAULT 0,
  date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""",
"""
CREATE TABLE IF NOT EXISTS categories(
  category_id SERIAL PRIMARY KEY,
  category_name VARCHAR(255) NOT NULL,
  description TEXT
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
  category_id INT REFERENCES categories(category_id) ON DELETE CASCADE,
  date_listed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  is_featured BOOLEAN DEFAULT FALSE,
  views_count INT DEFAULT 0 CHECK (views_count >= 0)
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
  status transaction_status NOT NULL
);
"""
    ,
"""
CREATE TABLE IF NOT EXISTS messages(
  message_id SERIAL PRIMARY KEY,
  sender_id INT REFERENCES users(user_id) ON DELETE CASCADE,
  receiver_id INT REFERENCES users(user_id) ON DELETE CASCADE,
  item_id INT REFERENCES items(item_id) ON DELETE CASCADE,
  content TEXT NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
    ,
"""
CREATE TABLE IF NOT EXISTS favorites(
  favorite_id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
  item_id INT REFERENCES items(item_id) ON DELETE CASCADE,
  date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(user_id, item_id)
);
"""
    ,
"""
CREATE TABLE IF NOT EXISTS reviews(
  review_id SERIAL PRIMARY KEY,
  reviewer_id INT REFERENCES users(user_id) ON DELETE CASCADE,
  reviewee_id INT REFERENCES users(user_id) ON DELETE CASCADE,
  transaction_id INT REFERENCES transactions(transaction_id) ON DELETE CASCADE,
  rating INT NOT NULL,
  comments TEXT,
  date_of_review TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT rating_check CHECK(rating BETWEEN 1 AND 5)
);
"""
    ,
"""
CREATE TABLE IF NOT EXISTS posts(
  post_id SERIAL PRIMARY KEY,
  poster_id INT REFERENCES users(user_id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  quantity INT NOT NULL CHECK (quantity > 0),
  points INT NOT NULL CHECK (points >= 0),
  zip_code VARCHAR(5) NOT NULL,
  expiration_date DATE NOT NULL,
  date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
]

index_queries = [
    "CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);",
    "CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);",
    "CREATE INDEX IF NOT EXISTS idx_items_trader_id ON items(trader_id);",
    "CREATE INDEX IF NOT EXISTS idx_items_category_id ON items(category_id);",
    "CREATE INDEX IF NOT EXISTS idx_transactions_sender_id ON transactions(sender_id);",
    "CREATE INDEX IF NOT EXISTS idx_transactions_receiver_id ON transactions(receiver_id);",
    "CREATE INDEX IF NOT EXISTS idx_messages_sender_id ON messages(sender_id);",
    "CREATE INDEX IF NOT EXISTS idx_messages_receiver_id ON messages(receiver_id);",
    "CREATE INDEX IF NOT EXISTS idx_reviews_reviewer_id ON reviews(reviewer_id);",
    "CREATE INDEX IF NOT EXISTS idx_reviews_reviewee_id ON reviews(reviewee_id);"
]

#alter_queries = [
#"""
#ALTER TABLE posts
#ADD COLUMN image_url TEXT;
#"""
#]
#execute the queries
try:
    for query in create_queries:
        cursor.execute(query)
    connection.commit()
    print("Tables create successfully")

    for index in index_queries:
        cursor.execute(index)
    connection.commit()
    print("Indexes created successfully")

    #for alter in alter_queries:
     #   cursor.execute(alter)
    #connection.commit()
    #print("Alterations created successfully")
except Exception as e:
    print(f"error creating tables: {e}")
    connection.rollback()
finally:
    #close the connection and cursor
    cursor.close()
    connection.close()
