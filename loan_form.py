import streamlit as st

def main():
    st.title("Smart Credit Risk Evolution")

    # Personal Information
    st.header("Personal Information")
    input_name = st.text_input('Enter your' 'name')
    st.header("Age")
    input_age = st.date_input('Enter your date of birth')
    st.header("Marital status")
    input_marital_status = st.selectbox('Select your marital status', ['Married', 'Single', 'Divorced'], index=0)
    st.header("Education")
    input_education_level= st.selectbox('Select your education level', ['PhD', 'Master', "Becheoler's", 'High School'], index=0)
    input_dependent=st.radio('Do you have any dependent',('Yes','No'))
    input_employment_type=st.selectbox('Select your employment type',['Full-time','Part-time','Self-employed','Unemployed'],index=0)
    input_co_signer=st.radio('Do you have any co-sign',('Yes','No'))
    input_month_employed=st.slider('Select your month employed', value=0, min_value=0, max_value=100, step=1)
    # Financial Information
    st.header("Financial Information")
    input_income = st.number_input('Enter your income', value=0)
    input_loan_amount = st.number_input('Enter the loan amount', value=0)
    input_credit_score = st.slider('Select your credit score', value=0, min_value=0, max_value=1000, step=1)
    input_no_of_creditLines = st.slider('Select your number of credit lines', value=0, min_value=0, max_value=100, step=1)  
    input_intrest_rate = st.slider('Select your intrest rate', value=0, min_value=0, max_value=100, step=1)
    input_loan_term = st.slider('Select your loan term', value=0, min_value=0, max_value=100, step=1)
    input_loan_purpose = st.selectbox('Select your loan purpose', ['Home', 'Auto', 'Buisness', 'Education','Other'], index=0)   
    input_mortgage = st.radio('Do you have any mortgage',('Yes','No'))

    # Predict button
    if st.button('Predict'):
        # Here you would call your prediction model
        # For demonstration purposes, we'll just display some dummy values
        prediction = "Approved"  # Dummy value
        probability = "85%"  # Dummy value

        st.write(f"Prediction: {prediction}")
        st.write(f"Probability: {probability}")

if __name__ == "__main__":
    main()
