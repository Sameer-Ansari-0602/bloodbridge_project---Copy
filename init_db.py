import os
import mysql.connector

db_config = {
    'host': os.environ.get("MYSQL_HOST", "localhost"),
    'user': os.environ.get("MYSQL_USER", "root"),
    'password': os.environ.get("MYSQL_PASSWORD", "Sameer@123"),
    'database': os.environ.get("MYSQL_DATABASE", "bloodbridge_db")
}

def init_db():
    try:
        # 1. Connect to MySQL Server
        print(f"Connecting to MySQL host: {db_config['host']}...")
        conn = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password']
        )
        cursor = conn.cursor()
        
        # 2. Create/Select Database dynamically
        target_db = db_config['database']
        print(f"Initializing database: {target_db}")
        
        # Create DB if it doesn't exist (safe for local & cloud)
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {target_db}")
        cursor.execute(f"USE {target_db}")
        
        # 3. Read and execute schema
        with open('schema.sql', 'r') as f:
            schema = f.read()
            
        # Split by semicolon to execute individual statements
        commands = schema.split(';')
        
        for command in commands:
            if command.strip():
                try:
                    cursor.execute(command)
                    print(f"Executed: {command[:50]}...")
                except Exception as e:
                    print(f"Error executing command: {e}")
                    
        conn.commit()
        conn.close()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Initialization Error: {e}")

if __name__ == '__main__':
    init_db()
