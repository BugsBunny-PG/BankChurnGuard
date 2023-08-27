import streamlit as st
import pandas as pd
import numpy as np
import pickle
model=pickle.load(open('customer_churn_model.pkl','rb'))
# Title
st.title('Customer Churn Prediction')
# sc=StandardScaler()
# Input fields
CreditScore= st.number_input('Credit Score')
CreditScore= int(CreditScore)
location = st.selectbox('Location', ['France', 'Germany', 'Spain'])
gender = st.selectbox('Gender', ['Male', 'Female'])
Age = st.number_input('Age', min_value=18, max_value=100, value=30)
Age= int(Age)
Tenure = st.number_input('Tenure', min_value=0, max_value=10, value=5)
Tenure= int(Tenure)
Balance = st.number_input('Account Balance', min_value=0.0, value=0.0)
Balance-float(Balance)
NumOfProducts = st.number_input('Number of Products', min_value=1, max_value=5, value=2)
NumOfProducts=int(NumOfProducts)
IsActiveMember = st.selectbox('Is Customer Active Member', [0, 1])
IsActiveMember=int(IsActiveMember)
EstimatedSalary = st.number_input('Estimated Salary', min_value=0.0, value=0.0)
EstimatedSalary=float(EstimatedSalary)
HasCrCard= st.selectbox('Has Credit Card?', [0, 1])
HasCrCard= int(HasCrCard)
submit=st.button("Predict Customer will Leave the bank or not?")
# Process inputs
if 	location=='Germany':
    	Geography=1
elif location=='France':
        Geography=0
else:
        Geography=2
       
if gender=='Female':
   Gender=0
else:
   Gender=1

# # Churn prediction button
if submit:
    # Perform churn prediction
    
    # Create a sample with numerical values for each feature
    sample_to_predict = np.array([[CreditScore, Geography,
       Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard,
       IsActiveMember, EstimatedSalary]])
    prediction = model.predict(sample_to_predict)
    if prediction[0] == 1:
        st.write("Churn")
    else:
        st.write("Not churn")
    
    
