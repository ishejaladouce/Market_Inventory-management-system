def connect_db():
    try:
        conn = pyscopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
            sslmode="REQUIRED"
        )
        return conn
    except Exception as e:
        print("Can't connect to the database.", e)
        return None