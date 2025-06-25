from train_model import train_model
from detector import detect_anomalies

if __name__ == "__main__":
    print("Training model...")
    train_model("user_behavior.csv")

    print("Detecting anomalies...")
    anomalies = detect_anomalies("new_user_data.csv")
    print(anomalies)