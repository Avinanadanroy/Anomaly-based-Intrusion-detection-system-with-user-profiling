import streamlit as st
import pandas as pd
from joblib import load
from datetime import datetime
import os

MODEL_PATH = "user_model.joblib"
LOG_FILE = "logs/anomalies.log"

def load_model(path):
    return load(path)

def detect_anomalies(df, model_data):
    scaler, model = model_data

    if 'user_id' in df.columns:
        user_ids = df['user_id']
        df = df.drop(['user_id'], axis=1)
    else:
        user_ids = pd.Series([f"user_{i}" for i in range(len(df))])

    X_scaled = scaler.transform(df)
    preds = model.predict(X_scaled)

    anomalies = df[preds == -1].copy()
    anomalies['user_id'] = user_ids[preds == -1].values
    return anomalies

def log_anomalies(anomalies_df):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        for _, row in anomalies_df.iterrows():
            ts = datetime.now().isoformat()
            data = row.to_dict()
            f.write(f"[{ts}] Anomaly Detected - User: {data['user_id']} | Data: {data}\n")

# --- Streamlit UI ---
st.set_page_config(page_title="Intrusion Detection Dashboard", layout="wide")
st.title("🛡️ Anomaly-based Intrusion Detection")
st.markdown("Upload user behavior data to detect unusual activity.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.subheader("📋 Uploaded Data")
    st.dataframe(data, use_container_width=True)

    try:
        model_data = load_model(MODEL_PATH)
        anomalies = detect_anomalies(data, model_data)

        if not anomalies.empty:
            st.subheader("🚨 Detected Anomalies")
            st.dataframe(anomalies, use_container_width=True)

            if st.button("Log Anomalies"):
                log_anomalies(anomalies)
                st.success("Anomalies logged to file.")
        else:
            st.success("✅ No anomalies detected.")

    except Exception as e:
        st.error(f"Error detecting anomalies: {e}")


