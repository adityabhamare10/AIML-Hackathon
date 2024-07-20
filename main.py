from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)

model_path = r'C:\Users\hp\Documents\AILML Hackathon\prediction_model.pkl'
model = joblib.load(model_path)

CORS(app)
@app.route('/predict-model', methods=['POST'])
def predict_model():


    data = request.get_json()
    print(data)

    processed_data = [
        data['age'],
        data['income'],
        data['loanAmount'],
        data['creditScore'],
        data['monthsEmployed'],
        data['numCreditLines'],
        data['interestRate'],
        data['loanTerm'],
        data['dtiRatio'],
        data['education'],
        data['employmentType'],
        data['maritalStatus'],
        data['hasMortgage'],
        data['hasDependents'],
        data['loanPurpose'],
        data['hasCoSigner']
    ]

    sample_data = np.array(processed_data).reshape(1, -1)

    probability = model.predict_proba(sample_data)[0, 1]
    prediction = model.predict(sample_data)[0]

    response = {
        "prediction": "Approved!!!!!!!" if prediction == 1 else "Denied",
        "probability": probability
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
