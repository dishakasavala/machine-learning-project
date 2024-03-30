import streamlit as st 
import pandas as pd 
import pickle as pk 

model=pk.load(open('model.pkl','rb')) 
scaler=pk.load(open('scaler.pkl','rb')) 

df=pd.read_csv('diamonds.csv')

st.header('Dimond Prediction App') 

cart = st.slider('Select carat',0.0,1.0)
cut_d = st.selectbox('Select Cut',df['cut'].unique())
color_d = st.selectbox('Select Colour',df['color'].unique())
clr_d = st.selectbox('Select clarity',df['clarity'].unique())
dep = st.slider('Select Depth',1.0,100.0)
tab = st.slider('Select Table',0,100)
x_data = st.slider('Select x value',0.0,11.0)
y_data = st.slider('Select y value',0.0,100.0)
z_data = st.slider('Select z value',0.0,50.0)

if st.button("Predict"): 
     pred_data = pd.DataFrame([[cart,cut_d,color_d,clr_d,dep,tab,x_data,y_data,z_data]],columns=['carat','cut','color','clarity','depth','table','x','y','z'])

     dimond_price = model.predict(pred_data)

     st.markdown('Dimond price = '+str(dimond_price[0]))