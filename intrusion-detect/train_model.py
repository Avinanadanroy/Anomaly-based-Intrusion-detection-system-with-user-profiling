import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from joblib import dump
import os

def train_model(data_path: str, model_path: str = "user_model.joblib"):
    df = pd.read_csv(data_path)

    if 'user_id' in df.columns:
        df = df.drop(['user_id'], axis=1)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(X_scaled)

    dump((scaler, model), model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model("user_behavior.csv")
