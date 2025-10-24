from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('rf_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    score = model.predict_proba(df)[0][1]  # probability of fraud
    return {"risk_score": score}

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # table of transactions & scores

if __name__ == "__main__":
    app.run(debug=True)
