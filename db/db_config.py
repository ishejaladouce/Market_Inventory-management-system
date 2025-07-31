"""
Database Configuration Module
============================

This module handles the database connection configuration for the Market Inventory System.
It uses PyMySQL to connect to a MySQL database hosted on Aiven cloud.

The connection uses environment variables for security and configuration flexibility.
"""

import os
import pymysql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def connect_db():
    """
    Establishes a connection to the MySQL database.
    
    Returns:
        pymysql.Connection: Database connection object if successful, None if failed
        
    Environment Variables Required:
        DB_HOST: Database server hostname
        DB_PORT: Database server port
        DB_USER: Database username
        DB_PASSWORD: Database password
        DB_NAME: Database name
    """
    try:
        # Create database connection with PyMySQL
        conn = pymysql.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            connect_timeout=10,
            ssl={'ssl': False}  # Disable SSL for Aiven compatibility
        )
        return conn
    except Exception as e:
        print("Can't connect to the database.", e)
        return None