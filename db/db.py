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

cursor = connection.cursor()
