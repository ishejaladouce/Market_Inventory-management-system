import os
import mysql.connector
from dotenv import load_dotenv

#Load Enirnoment variables from .env file
load_dotenv()

def connect_db():
    try:
        conn = mysql.connector.connect( 
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            ssl_disabled=False
        )
        return conn
    except Exception as e:
        print("Can't connect to the database.", e)
        return None