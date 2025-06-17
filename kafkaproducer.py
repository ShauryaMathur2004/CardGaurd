import pandas as pd
from kafka import KafkaProducer
import json
import time

# Load the actual dataset
df = pd.read_csv('cleaned_data.csv')  # Make sure the path is correct

# Setup Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send each row as a message to Kafka
for _, row in df.iterrows():
    data = row.to_dict()
    producer.send('fraud-detection', value=data)
    print(f"Sent: {data}")
    time.sleep(2)  # Adjust delay as needed
