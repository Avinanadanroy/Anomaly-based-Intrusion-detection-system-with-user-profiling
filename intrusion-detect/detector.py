import pandas as pd
from joblib import load
from utils import log_anomaly

def detect_anomalies(new_data_path: str, model_path: str = "user_model.joblib"):
    from joblib import load
    import pandas as pd
    from utils import log_anomaly

    scaler, model = load(model_path)
    df = pd.read_csv(new_data_path)

    if 'user_id' in df.columns:
        user_ids = df['user_id']
        df = df.drop(['user_id'], axis=1)
    else:
        user_ids = pd.Series([f"user_{i}" for i in range(len(df))])

    if 'file_access' in df.columns:
        df = df.drop(['file_access'], axis=1)

    X_scaled = scaler.transform(df)
    predictions = model.predict(X_scaled)  # -1: anomaly, 1: normal

    anomalies = df[predictions == -1].copy()
    anomalies['user_id'] = user_ids[predictions == -1].values

    for idx in anomalies.index:
        log_anomaly(anomalies.loc[idx]['user_id'], anomalies.loc[idx].to_dict())

    return anomalies[['user_id'] + df.columns.tolist()]
            
if __name__ == "__main__":
    anomalies = detect_anomalies("new_user_data.csv")
    print("Anomalies found:")
    print(anomalies)
    print("No anomalies detected.")
    print("Anomalies logged.")