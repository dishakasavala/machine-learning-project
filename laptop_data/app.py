import streamlit as st 
import pandas as pd 
import pickle as pk 

model=pk.load(open('model.pkl','rb')) 
scaler=pk.load(open('scaler.pkl','rb'))  

st.header('Laptop Prediction App') 

df = pd.read_csv('laptop_data (1).csv')

def get_cpu_name(cpu_na):
     words = cpu_na.split()  # Split into a list of words
     return ' '.join(words[:3]).strip()
df['cpu_name'] = df['cpu_name'].apply(get_cpu_name)

com_s = st.selectbox('Select Company',df['Company'].unique())
typ_s = st.selectbox('Select Type Name',df['TypeName'].unique())
ram_s = st.selectbox('Select Ram',[2,4,6,8,12,16,24,32,64])
ops_s = st.selectbox('Select Opstype',df['OpSys'].unique())
we_s = st.slider('Select Weight',0.0,5.0)
touch_s = st.selectbox('Touchscreen yes or not',['Yes','No'])
ips_s = st.radio('Ips panel yes or not',['Yes','No'],)
ppi_s = st.selectbox('Select PPT Rate ',[226.98300468, 127.67794013, 141.21199808, 220.53462387,100.45466986, 157.35051215, 226.41554717, 165.63211805,135.09421119, 127.33567457, 111.93520356, 276.05353009,90.58340172, 224.17380908, 200.84255994, 352.46514721,199.69207064, 119.72321577, 331.2642361 , 316.96506044,282.42399616, 209.80068286, 106.11306214, 254.67134914,158.48253022, 117.82653006, 176.23257361, 267.33843603,169.78089943, 189.90579052, 234.50740003, 125.36742799,107.98564559, 161.72539084, 146.86047801, 111.14133687,194.94753718, 234.97676481, 220.84282407])
cpu_n = st.selectbox('Select Cpu name',df['cpu_name'].unique())
ssd_s = st.selectbox('Select SSD drive',[0,8,16,32,64,128,180,240,256,512,768,1024])
hhd_s = st.selectbox('Select HDD drive',[0,32,128,500,1024,2048])
flash_s = st.selectbox('Select Flash Storage drive',[0,16,32,64,128,256,512])
hy_s = st.selectbox('Select Hybrid drive',[0,16,32,64,128,256,512])
gpu_s = st.selectbox('Select GPU name',df['gpu_brand'].unique())

if touch_s == "Yes":
     t_s = 0
else:
     t_s = 1

if ips_s == "Yes":
     i_s = 0
else:
     i_s = 1