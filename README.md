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

intrusion-detect/<br>
├── pycache/ &nbsp;&nbsp;&nbsp;&nbsp;# Compiled Python files<br>
├── logs/ &nbsp;&nbsp;&nbsp;&nbsp;# Logs directory<br>
│&nbsp;&nbsp;&nbsp;&nbsp;└── anomalies.log &nbsp;&nbsp;&nbsp;&nbsp;# Log of detected anomalies<br>
<br>
├── dashboard.py &nbsp;&nbsp;&nbsp;&nbsp;# Visualization/dashboard logic<br>
├── detector.py &nbsp;&nbsp;&nbsp;&nbsp;# Anomaly detection logic<br>
├── main.py &nbsp;&nbsp;&nbsp;&nbsp;# Entry point to run the system<br>
├── train_model.py &nbsp;&nbsp;&nbsp;&nbsp;# Model training script<br>
├── utils.py &nbsp;&nbsp;&nbsp;&nbsp;# Utility functions<br>
├── new_user_data.csv &nbsp;&nbsp;&nbsp;&nbsp;# New data to check for anomalies<br>
├── user_behavior.csv &nbsp;&nbsp;&nbsp;&nbsp;# Historical normal user behavior data<br>
├── user_model.joblib &nbsp;&nbsp;&nbsp;&nbsp;# Trained machine learning model<br>
├── requirements.txt &nbsp;&nbsp;&nbsp;&nbsp;# Python dependencies<br>
├── run.txt &nbsp;&nbsp;&nbsp;&nbsp;# Run instructions or notes<br>
└── README.md &nbsp;&nbsp;&nbsp;&nbsp;# Project documentation<br>


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

