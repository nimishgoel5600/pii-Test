import psycopg2
from .config import PG_CONFIG

def connect():
    conn = psycopg2.connect(**PG_CONFIG)
    return conn

def insert_data(data):
    conn = connect()
    cursor = conn.cursor()
    # SQL query to create the 'user_logins' table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_logins (
        user_id VARCHAR(128),
        device_type VARCHAR(32),
        masked_ip VARCHAR(256),
        masked_device_id VARCHAR(256),
        locale VARCHAR(32),
        app_version VARCHAR(32)
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print(data)
    insert_query = f"""
        INSERT INTO user_logins (
            user_id,
            device_type,
            masked_ip,
            masked_device_id,
            locale,
            app_version
        ) VALUES (
            '{data['user_id']}', 
            '{data['device_type']}', 
            '{data['masked_ip']}',
            '{data['masked_device_id']}', 
            '{data['locale']}', 
            '{data['app_version']}');
    """
    # write the insert query
    cursor.execute(insert_query)
    conn.commit()
    conn.commit()
    cursor.close()
    conn.close()
