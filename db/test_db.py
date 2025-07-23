from db_config import connect_db

def test_connection():
    conn = connect_db()
    if conn:
        print("Connected sucessfully to Aiven DB!")
        conn.close()
    else:
        print("Failed to connect to Aiven DB.")

test_connection()