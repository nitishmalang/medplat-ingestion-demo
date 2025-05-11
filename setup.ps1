
Write-Output "Stopping and removing existing containers..."
docker rm -f kafka zookeeper postgres

Write-Output "Creating Docker network..."
docker network create kafka-net

Write-Output "Starting Zookeeper..."
docker run -d --name zookeeper --network kafka-net -p 2181:2181 -e ZOOKEEPER_CLIENT_PORT=2181 -e ZOOKEEPER_TICK_TIME=2000 zookeeper

Write-Output "Starting Kafka..."
docker run -d --name kafka --network kafka-net -p 9092:9092 -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 -e KAFKA_BROKER_ID=1 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 --memory=2g confluentinc/cp-kafka

Write-Output "Starting PostgreSQL..."
docker run -d --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=pass postgres

Write-Output "Waiting for services to start (30 seconds)..."
Start-Sleep -Seconds 30

Write-Output "Setup complete! Run producer.py and consumer.py."