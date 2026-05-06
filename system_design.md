import json
from kafka import KafkaConsumer
from app.graph.ingest import ingest_event

consumer = KafkaConsumer(
    "temporal-events",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)

for message in consumer:
    ingest_event(message.value)