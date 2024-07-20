import streamlit as st
import requests
import datetime


# def calculate_age(born):
#     today = datetime.date.today()
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def main():
    st.title("Smart Credit Risk Evolution")

    # Personal Information
    st.header("Personal Information")
    input_name = st.text_input('Enter your name')
    st.header("Enter Age: ")
    # input_dob = st.date_input('Enter your date of birth')
    input_age = st.slider("Age", value=18, min_value=18, max_value=70, step=1)
    st.header("Marital status")
    input_marital_status = st.selectbox('Select your marital status', ['Married', 'Single', 'Divorced'], index=0)
    st.header("Education")
    input_education_level = st.selectbox('Select your education level', ['PhD', 'Master', "Bachelor's", 'High School'],
                                         index=0)
    input_dependent = st.radio('Do you have any dependents', ('Yes', 'No'))
    input_employment_type = st.selectbox('Select your employment type',
                                         ['Full-time', 'Part-time', 'Self-employed', 'Unemployed'], index=0)
    input_co_signer = st.radio('Do you have any co-signer', ('Yes', 'No'))
    input_month_employed = st.slider('Select your months employed', value=0, min_value=0, max_value=100, step=1)

    # Financial Information
    st.header("Financial Information")
    input_income = st.number_input('Enter your income', value=0)
    input_loan_amount = st.number_input('Enter the loan amount', value=0)
    input_credit_score = st.slider('Select your credit score', value=0, min_value=0, max_value=1000, step=1)
    input_no_of_creditLines = st.slider('Select your number of credit lines', value=0, min_value=0, max_value=100,
                                        step=1)
    input_interest_rate = st.slider('Select your interest rate', value=0, min_value=0, max_value=100, step=1)
    input_loan_term = st.slider('Select your loan term', value=0, min_value=0, max_value=100, step=1)
    input_loan_purpose = st.selectbox('Select your loan purpose', ['Home', 'Auto', 'Business', 'Education', 'Other'],
                                      index=0)
    input_mortgage = st.radio('Do you have any mortgage', ('Yes', 'No'))

    # Map categorical variables to numerical values
    education_mapping = {"PhD": 3, "Master's": 2, "Bachelor's": 0, "High School": 1}
    employment_mapping = {'Full-time': 3, 'Part-time': 0, 'Self-employed': 2, 'Unemployed': 1}
    marital_mapping = {'Married': 0, 'Divorced': 1, 'Single': 2}
    yes_no_mapping = {'Yes': 1, 'No': 0}
    purpose_mapping = {'Home': 1, 'Auto': 4, 'Business': 0, 'Education': 2, 'Other': 3}

    # Predict button
    if st.button('Predict'):
        # Prepare the data to send to the Flask server
        data = {
            'age': input_age,
            'income': input_income,
            'loanAmount': input_loan_amount,
            'creditScore': input_credit_score,
            'monthsEmployed': input_month_employed,
            'numCreditLines': input_no_of_creditLines,
            'interestRate': input_interest_rate,
            'loanTerm': input_loan_term,
            'dtiRatio': input_loan_amount / input_income if input_income > 0 else 0,  # Example DTI ratio calculation
            'education': education_mapping[input_education_level],
            'employmentType': employment_mapping[input_employment_type],
            'maritalStatus': marital_mapping[input_marital_status],
            'hasMortgage': yes_no_mapping[input_mortgage],
            'hasDependents': yes_no_mapping[input_dependent],
            'loanPurpose': purpose_mapping[input_loan_purpose],
            'hasCoSigner': yes_no_mapping[input_co_signer]
        }

        with st.spinner('Calculating...'):
            # Send data to the Flask server
            response = requests.post("http://127.0.0.1:5000/predict-model", json=data)
            result = response.json()

        # Display the prediction and probability
        st.success('Here is your Result')
        # st.balloons()
        st.write(f"Prediction: {result['prediction']}")
        st.write(f"Probability: {result['probability']}")


if __name__ == "__main__":
    main()
