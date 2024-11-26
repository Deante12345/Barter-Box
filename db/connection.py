import psycopg2
from psycopg2.extras import RealDictCursor
import db.config


def get_connection():
     return psycopg2.connect(
        host=db.config.DB_HOST,
        port=db.config.DB_PORT,
        dbname=db.config.DB_NAME,
        user=db.config.DB_USER,
        password=db.config.DB_PASSWORD,
        cursor_factory=RealDictCursor
     )
