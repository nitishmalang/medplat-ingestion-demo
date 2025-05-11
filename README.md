# MedPlat Ingestion Demo

This project is a demo for C4GT DMP 2025 issue #544: Unified Data Ingestion Framework. It implements a real-time healthcare data ingestion pipeline using Kafka and PostgreSQL to process patient vitals from a mobile app, aligning with MedPlat's goal of scalable, decoupled data ingestion. The pipeline reads patient data (e.g., heart rate, blood pressure, temperature) from a JSON source, streams it through Kafka, and stores it in a PostgreSQL database, demonstrating a robust framework for healthcare data processing.

## Purpose
The demo showcases:
- **Real-Time Ingestion**: Streams patient vitals using Kafka for high-throughput processing.
- **Scalability**: Decouples data production and consumption via Kafka’s `patient_data` topic.
- **Healthcare Relevance**: Processes structured patient data, suitable for MedPlat’s ecosystem.
- **Ease of Use**: Automates setup with a PowerShell script (`setup.ps1`) and provides clear instructions.

The pipeline flow is:
1. **Data Source**: `mobile_app.json` contains patient vitals (e.g., `patient_id`, `heart_rate`).
2. **Producer**: `producer.py` sends data to Kafka’s `patient_data` topic (`localhost:9092`).
3. **Kafka**: Streams data in real-time.
4. **Consumer**: `consumer.py` pulls data from Kafka and saves it to PostgreSQL (`localhost:5432`).
5. **PostgreSQL**: Stores data in the `patient_data` table with columns `id`, `patient_id`, `timestamp`, `heart_rate`, `blood_pressure`, `temperature`, and `location`.

## Prerequisites
- Docker Desktop (Windows)
- Python 3.9+
- PowerShell
- Git

## Setup
1. Clone the repository:

   `git clone https://github.com/[your-username]/medplat-ingestion-demo`
   `cd medplat-ingestion-demo`

## Create and activate a virtual environment

    `python -m venv venv`
    `.\venv\Scripts\activate`

## Install dependencies

    `pip install -r requirements.txt`

## Run the setup script to start Zookeeper, Kafka, and PostgreSQL

     `.\setup.ps1`


## Setup Complete

![alt text](<WhatsApp Image 2025-05-11 at 13.30.33_ad72791a.jpg>) 
shows successful setup of Zookeeper, Kafka, and PostgreSQL.



# Running the Demo

## Start the consumer to listen for data on the patient_data topic (in one PowerShell)

`python scripts/consumer.py`

![alt text](<WhatsApp Image 2025-05-11 at 13.31.54_5909605e.jpg>) 
shows consumer.py ready to receive Kafka messages



## Send data to Kafka with the producer (in another PowerShell)

`python scripts/producer.py`

![alt text](<WhatsApp Image 2025-05-11 at 13.32.44_77306c16.jpg>)
shows producer.py sending data to Kafka.
Consumer Received

![alt text](<WhatsApp Image 2025-05-11 at 14.06.42_394d570b.jpg>) 
shows consumer.py receiving data and saving it to PostgreSQL.

## Verify data in PostgreSQL

`docker exec -it postgres psql -U postgres
SELECT * FROM patient_data;
\q`

![alt text](<WhatsApp Image 2025-05-11 at 14.10.49_4b4610b5.jpg>) 
shows the ingested patient data in PostgreSQL.


# Files

mobile_app.json: JSON contract for healthcare data (patient vitals).

pipeline.png: Diagram of the data pipeline (see below).

scripts/producer.py: Sends patient data to Kafka.

scripts/consumer.py: Consumes data from Kafka and saves to PostgreSQL.

setup.ps1: PowerShell script to start Zookeeper, Kafka, and PostgreSQL.

requirements.txt: Python dependencies (kafka-python, psycopg2-binary).








   