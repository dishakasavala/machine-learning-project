import streamlit as st 
import pandas as pd 
import pickle as pk 
from sklearn.preprocessing import StandardScaler

model=pk.load(open('model.pkl','rb')) 
scaler=pk.load(open('scaler.pkl','rb')) 

df = pd.read_csv('quikr_car.csv')

def get_car_name(car_name):
     words = car_name.split()  # Split into a list of words
     return ' '.join(words[:3]).strip()
df['name'] = df['name'].apply(get_car_name)

b_name = st.selectbox('Select Brand Name',df['name'].unique())
yea = st.slider('Select year',2015,2023)
km = st.slider('Select kilometer driven',0,10000000)
fu = st.selectbox('Select Fule type',['Petrol','Diesel'])

if st.button('Price'):
     prect_data = pd.DataFrame([[b_name,yea,km,fu]],
                               columns=['name','year','kms_driven','fuel_type'])
     
    
     car_price = model.predict(prect_data)

     st.markdown('Car price  = '+str(car_price[0]))