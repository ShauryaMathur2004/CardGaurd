import streamlit as st
from kafka import KafkaConsumer
import json
import joblib
import pandas as pd

# Load ML model
model = joblib.load("logistic_model.pkl")

# Set page config
st.set_page_config(page_title="Fraud Detect Dashboard", layout="wide")
st.title("🚨 Real-time Fraud Detection Dashboard")

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'fraud-detection',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Poll for the latest message
message_pack = consumer.poll(timeout_ms=3000, max_records=1)
latest_transaction = None

for tp, messages in message_pack.items():
    for message in messages:
        latest_transaction = message.value

# Display transaction and prediction
if latest_transaction:
    st.subheader("Latest Transaction:")
    st.json(latest_transaction)

    features = pd.DataFrame([latest_transaction])
    prediction = model.predict(features)[0]
    result = "Fraud" if prediction == 1 else "Legit"

    st.markdown(f"### 🧠 Prediction: **{result}**")
else:
    st.warning("No new message received.")
