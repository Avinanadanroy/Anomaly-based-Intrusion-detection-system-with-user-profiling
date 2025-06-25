# Anomaly-based-Intrusion-detection-system-with-user-profiling

This project implements an Anomaly-Based Intrusion Detection System (AIDS) using user behavior profiling. It detects unusual user activities by training on normal behavior and flagging deviations as anomalies.

## 🧠 Features

- Train a machine learning model on user behavior (`user_behavior.csv`)
- Detect anomalies in new user data (`new_user_data.csv`)
- Log suspicious activities to `logs/anomalies.log`
- Visualize results via `dashboard.py`
- Modular structure for training, detection, and utility functions

---

## 📁 Project Structure

intrusion-detect/
│
├── pycache/ # Compiled Python files
├── logs/ # Logs directory
│ └── anomalies.log # Log of detected anomalies
│
├── dashboard.py # Visualization/dashboard logic
├── detector.py # Anomaly detection logic
├── main.py # Entry point to run the system
├── train_model.py # Model training script
├── utils.py # Utility functions
├── new_user_data.csv # New data to check for anomalies
├── user_behavior.csv # Historical normal user behavior data
├── user_model.joblib # Trained machine learning model
├── requirements.txt # Python dependencies
├── run.txt # Run instructions or notes
└── README.md # Project documentation

---

### Prerequisites

Install dependencies with:

```bash
pip install -r requirements.txt

---

### Running the Project

1. Train the Model:
    ```python train_model.py

2. Run Anomaly Detection:
    ```python main.py    

3. View Dashboard:    
    ```python dashboard.py

---

### Files Description

main.py: Orchestrates model loading, data input, and detection.

train_model.py: Trains a model on known good behavior and saves it as user_model.joblib.

detector.py: Contains logic to compare new behavior to the trained model.

dashboard.py: Provides a UI/visual representation of detection results.

utils.py: Helper functions used across modules.

---

### Datasets
user_behavior.csv: Training data containing normal user actions.

new_user_data.csv: New behavior logs to be analyzed for anomalies.

---

### Logs
logs/anomalies.log: Logs all detected anomalies with timestamps.


---

### Dependencies
Listed in requirements.txt. Common libraries might include:

scikit-learn

joblib

pandas

matplotlib or plotly

