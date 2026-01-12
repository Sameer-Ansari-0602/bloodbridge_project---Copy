import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root', 
    'password': 'Sameer@123', 
    'database': 'bloodbridge_db'
}

def init_db():
    try:
        # Connect to server first to create DB if not exists
        conn = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password']
        )
        cursor = conn.cursor()
        
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
