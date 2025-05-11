from kafka import KafkaProducer
import json
import time

try:
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
except Exception as e:
    print(f"Error connecting to Kafka: {e}")
    exit(1)

data = {
    "patient_id": "P123",
    "timestamp": "2025-05-01T10:00:00",
    "vitals": {
        "heart_rate": 80,
        "blood_pressure": "120/80",
        "temperature": 36.6
    },
    "location": "Clinic A"
}

print("Sending data to patient_data topic...")
producer.send('patient_data', json.dumps(data).encode('utf-8'))
producer.flush()
print("Data sent!")