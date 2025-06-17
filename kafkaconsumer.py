from kafka import KafkaConsumer
import json

import pandas as pd
import joblib

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("Waiting for messages...")



model = joblib.load('logistic_model.pkl')  # or 'random_forest_model.pkl'
columns = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
           'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 
           'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 
           'V28', 'Amount']


for message in consumer:
    data = message.value

    # Convert to DataFrame
    df = pd.DataFrame([data], columns=columns)

    # Predict
    prediction = model.predict(df)[0]
    result = "FRAUD" if prediction == 1 else "SAFE"

    print(f"Transaction: {data}")
    print(f"Prediction: {result}")
