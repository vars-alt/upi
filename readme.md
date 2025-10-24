# UPI Fraud Detection System

A machine learning system to detect suspicious UPI transactions and provide real-time risk scores via a Flask dashboard.

## Project Overview
The system processes transaction data and flags potentially fraudulent activity using a Random Forest classifier. A lightweight Flask dashboard allows monitoring of transactions and alerts in real-time.

### Features
- Real-time fraud detection API for UPI transactions.
- ML pipeline using Random Forest for classification.
- Feature engineering and hyperparameter tuning for improved accuracy.
- Lightweight Flask dashboard for visualizing transaction risk.
- Scalable architecture suitable for integration with cloud services.

### Tools & Technologies
- Python 3.x
- pandas, scikit-learn
- Flask
- joblib (model serialization)
- Optional: Docker for containerized deployment


## Folder Structure
upi_fraud/
- app.py # Flask API & dashboard
-  model.py # ML pipeline
- requirements.txt

  
