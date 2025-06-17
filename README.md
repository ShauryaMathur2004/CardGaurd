# 💳 CardGuard: Real-Time Credit Card Fraud Detection Dashboard

CardGuard is a real-time fraud detection system designed to process streaming transaction data using Apache Kafka, apply a trained machine learning model, and display predictions via a sleek Streamlit-based dashboard.

---

## 📂 Project Structure

```
fraud-detect-dashboard/
│
├── app/                          # Streamlit app and core logic
│   ├── app.py                   # Streamlit UI file
│   ├── consumer.py              # Kafka consumer logic
│   ├── producer.py              # Kafka producer logic using real dataset
│   ├── logistic_model.pkl       # Trained ML model (e.g., Logistic Regression)
│   └── cleaned_data.csv         # Source transaction dataset
│
├── docker-compose.yml           # Container orchestration
├── Dockerfile                   # Docker config for Python environment
└── README.md                    # Project documentation
```

---

## 🛠️ How It Works

### 🔁 Kafka Message Flow

- `producer.py`: Reads transactions from `cleaned_data.csv` and sends each as a JSON message to the Kafka topic `fraud-detection`.
- `consumer.py`: Consumes messages from Kafka and makes predictions using a pre-trained model.
- `app.py`: Streamlit frontend that polls for the latest transaction, predicts if it's FRAUD or SAFE, and displays the result.

### 🧠 Machine Learning Model

- Trained on the [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud).
- Features include anonymized V1–V28 PCA components, Time, and Amount.
- Model used: Logistic Regression (saved as `logistic_model.pkl` using `joblib`).

---

## 🚀 Setup & Running Locally

### 🔧 Prerequisites

- Docker Desktop
- Python 3.10+
- pip packages: `pandas`, `joblib`, `kafka-python`, `streamlit`

### 🐳 1. Start Kafka + Zookeeper with Docker

```bash
docker-compose up -d --build
```

### ▶️ 2. Run the Kafka Producer (in one terminal)

```bash
cd app
python producer.py
```

### 🧾 3. Run the Streamlit Dashboard (in another terminal)

```bash
streamlit run app.py
```

---

## 🎥 Preview & Outputs

- Real-time transaction stream.
- Model prediction shown for every new transaction.
- UI updates dynamically.
- Screenshots and videos included in `media/` folder (attach your screenshots or .mp4 here).

---

## 🧪 Key Features

- ⚡ Real-time fraud detection pipeline
- 📊 Clean, interactive UI using Streamlit
- 🐍 Pythonic end-to-end deployment
- 🧵 Kafka for asynchronous message processing

---

## 📸 Screenshots & Demo

> Attach your output images and videos here, e.g.

![Dashboard Screenshot](https://drive.google.com/drive/folders/1x3gaJQIshcDkA9Q1vqyLhY7Fcst0H3ud?usp=sharing)

📹 [Watch Demo Video](https://drive.google.com/drive/folders/1x3gaJQIshcDkA9Q1vqyLhY7Fcst0H3ud?usp=sharing)

---

## 📎 Acknowledgments

- Dataset: [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- Apache Kafka for real-time stream processing
- Streamlit for quick deployment


