import streamlit as st 
import pandas as pd 
import pickle as pk 

classifer=pk.load(open('model.pkl','rb')) 
scaler=pk.load(open('scaler.pkl','rb')) 

st.header('Loan Prediction App') 

gen = st.selectbox('Choose Gender',['Male','Female']) 
mar = st.selectbox('Married status',['Married','Not Married']) 
no_of_dep = st.slider('Choose No of dependents', 0, 5) 
eda = st.selectbox('Choose Education',['Graduated','Not Graduated']) 
self_emp = st.selectbox('Self Emoployed ?',['Yes','No']) 
aapli_income = st.slider('Choose Applicatincome Income', 0, 50000)
coaapli_income = st.slider('Choose Coapplicatincome Income', 0, 30000)
Loan_Amount = st.slider('Choose Loan Amount', 0, 100000) 
Loan_Dur = st.slider('Choose Loan Amount Term', 0, 400)
cre_hist = st.selectbox('Choose Credit History',['0','1']) 
pro_are = st.selectbox('Choose property area',['Urban','Rural','Semiurban'])

if eda =='Graduated': 
    grad_s =0 
else: 
    grad_s = 1 
 
if self_emp =='No': 
    emp_s =0 
else: 
    emp_s = 1 

if gen =='Male': 
    gen_s =0 
else: 
    gen_s = 1 

if mar =='Married': 
    mar_s =0 
else: 
    mar_s = 1 

if cre_hist =='0': 
    cre_s =0 
else: 
    cre_s = 1 
    
if pro_are =='Urban': 
    pro_s =0 
elif pro_are=='Rural': 
    pro_s = 1 
else:
    pro_s = 2

if st.button("Predict"): 
    pred_data = pd.DataFrame([[gen_s,mar_s,no_of_dep,grad_s,emp_s,aapli_income,coaapli_income,Loan_Amount,Loan_Dur,cre_s,pro_s]], columns=['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']) 
    red_data = scaler.transform(pred_data) 
    predict = classifer.predict(pred_data) 
    if predict[0] == 1: 
        st.markdown('Loan Is Approved') 
    else: 
        st.markdown('Loan Is Rejected') 
  