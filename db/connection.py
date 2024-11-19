import psycopg2
from psycopg2.extras import RealDictCursor
import db.config


def get_connection():
     return psycopg2.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        cursor_factory=RealDictCursor
     )
