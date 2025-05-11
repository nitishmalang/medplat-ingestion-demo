from kafka import KafkaConsumer
import json
import psycopg2

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="pass",
        host="localhost",  # Use localhost since port is mapped
        port="5432"
    )
    cursor = conn.cursor()
    print("Connected to PostgreSQL!")
except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")
    exit(1)

# Create table
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patient_data (
            id SERIAL PRIMARY KEY,
            patient_id VARCHAR(50),
            timestamp VARCHAR(50),
            heart_rate INTEGER,
            blood_pressure VARCHAR(20),
            temperature FLOAT,
            location VARCHAR(100)
        )
    """)
    conn.commit()
    print("Table patient_data created or already exists!")
except Exception as e:
    print(f"Error creating table: {e}")
    conn.rollback()
    exit(1)

# Connect to Kafka
try:
    consumer = KafkaConsumer('patient_data', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    print("Connected to Kafka!")
except Exception as e:
    print(f"Error connecting to Kafka: {e}")
    exit(1)

print("Listening for data on patient_data topic...")
for msg in consumer:
    try:
        data = json.loads(msg.value.decode('utf-8'))
        print(f"Received: {data}")
        cursor.execute("""
            INSERT INTO patient_data (patient_id, timestamp, heart_rate, blood_pressure, temperature, location)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data['patient_id'],
            data['timestamp'],
            data['vitals']['heart_rate'],
            data['vitals']['blood_pressure'],
            data['vitals']['temperature'],
            data['location']
        ))
        conn.commit()
        print("Saved to PostgreSQL!")
    except Exception as e:
        print(f"Error processing message: {e}")
        conn.rollback()

# Close connections (optional, as script runs indefinitely)
cursor.close()
conn.close()