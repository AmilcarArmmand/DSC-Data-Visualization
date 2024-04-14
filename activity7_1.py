import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Diabetes Data')
data_URL = 'https://storage.googleapis.com/scsu-data-science/diabetes_nan.csv'
df = pd.read_csv(data_URL)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.markdown('---')
st.subheader('Glucose Levels Based on Diabetic Status')

status = st.radio('Select diabetic vs. non-diabetic', ('Diabetic', 'Non-diabetic'))

if status == 'Non-diabetic':
    df = df.loc[df['Outcome']== 0]
else:
    df = df.loc[df['Outcome']== 1]

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel('Glucose Level')
ax.set_ylabel('Frequency')
ax.hist(df['Glucose'], bins = 30)
st.pyplot(fig)
