# Smart Credit Risk Evolution

Smart Credit Risk Evolution is a web application that evaluates the credit risk of loan applicants. Using a machine learning model, it predicts whether a loan application should be approved and provides the probability of approval based on various applicant details.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Smart Credit Risk Evolution leverages a logistic regression model to assess the risk associated with loan applicants. The system provides a frontend for users to input their details and receive a prediction on their loan application status along with the probability of approval.

## Features

- Input personal and financial information through a web interface.
- Receive real-time predictions and approval probabilities.
- User-friendly interface built with Streamlit.
- Backend powered by Flask and a logistic regression model.

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/smart-credit-risk-evolution.git
    cd smart-credit-risk-evolution
    ```

2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Prepare the Model:

    Ensure you have the dataset (`Loan_default.csv`) in the appropriate directory. Run the Jupyter Notebook (`model_training.ipynb`) to train and save the model:

    ```sh
    jupyter notebook model_training.ipynb
    ```

    This will generate a `prediction_model.pkl` file in the specified directory.

4. Configure the Flask server:

    Update the `model_path` in the Flask script to the location of your `prediction_model.pkl`.

    ```python
    model_path = r'C:\Users\hp\Documents\AILML Hackathon\prediction_model.pkl'
    ```

5. Run the Flask server:

    ```sh
    python flask_server.py
    ```

6. Run the Streamlit app:

    ```sh
    streamlit run streamlit_app.py
    ```

## Usage

- Open the Streamlit app in your web browser. By default, it runs at [http://localhost:8501](http://localhost:8501).
- Input your personal and financial information into the provided form.
- Click the "Predict" button to receive your loan approval prediction and probability.

## Model Training

The model is trained using a logistic regression algorithm on a dataset of loan applications. The training process involves:

- Preprocessing the data by converting categorical variables to numerical values.
- Splitting the data into training and testing sets.
- Training the logistic regression model.
- Saving the trained model for use in the Flask server.

### Example Code for Model Training

```python
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset
df = pd.read_csv("Loan_default.csv")

# Preprocess the dataset
df = df.drop(columns=['LoanID'])
df.replace({"Education": {"Bachelor's": 0, 'High School': 1, "Master's": 2, 'PhD': 3}}, inplace=True)
df.replace({"EmploymentType": {'Part-time': 0, 'Unemployed': 1, 'Self-employed': 2, 'Full-time': 3}}, inplace=True)
df.replace({"MaritalStatus": {'Married': 0, 'Divorced': 1, 'Single': 2}}, inplace=True)
df.replace({"HasMortgage": {'No': 0, 'Yes': 1}}, inplace=True)
df.replace({"HasDependents": {'No': 0, 'Yes': 1}}, inplace=True)
df.replace({"LoanPurpose": {'Business': 0, 'Home': 1, 'Education': 2, 'Other': 3, 'Auto': 4}}, inplace=True)
df.replace({"HasCoSigner": {'No': 0, 'Yes': 1}}, inplace=True)

# Split the data
X = df.drop(columns=['Default'], axis=1)
Y = df['Default']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=2)

# Train the model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Save the model
joblib.dump(model, 'prediction_model.pkl')
```
