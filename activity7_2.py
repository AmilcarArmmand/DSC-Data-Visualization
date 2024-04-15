import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Kent County Housing Data :house:')
data_URL = 'https://storage.googleapis.com/scsu-data-science/kc_house_mini.csv'
df = pd.read_csv(data_URL, thousands=',')

df = df.rename(columns={'long': 'lon'})

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.markdown('---')

st.subheader('\nBedroom selectbox')
bedrooms = st.selectbox(
    'How many bedrooms would you like?',
    (1, 2, 3, 4, 5))
st.write('You selected:', bedrooms)

if bedrooms == 1:
    df = df.loc[df['bedrooms']== 1]
elif bedrooms == 2:
    df = df.loc[df['bedrooms']== 2]
elif bedrooms == 3:
    df = df.loc[df['bedrooms']== 3]
elif bedrooms == 4:
    df = df.loc[df['bedrooms']== 4]
else:
    df = df.loc[df['bedrooms']== 5]

st.markdown('---')
st.subheader('\nPrice slider :heavy_dollar_sign:')
price_range = st.slider('Select a price range:',
                        min_value = 0,
                        max_value = 4000000,
                        value = [50000, 3500000],
                        step = 10000)
st.write("Price range", price_range)

st.markdown('---')
df_map = df.loc[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]
st.map(df_map)
