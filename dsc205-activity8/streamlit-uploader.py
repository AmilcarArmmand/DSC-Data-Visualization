import streamlit as st
import pandas as pd
from pandas.api.types import is_numeric_dtype
from io import StringIO
import matplotlib.pyplot as plt

st.title('Histogram plotter')

uploaded_file = st.file_uploader("Choose a file")
# Upload the file after the user makes a selection.
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # display the dataframe in the app
    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        with st.form(key='Form1'):
            col1 = st.text_input('Input column name:')
            submitted1 = st.form_submit_button(label='Submit 1')

    with col2:
        with st.form(key='Form2'):
            col2 = st.text_input('Input column name:')
            submitted2 = st.form_submit_button(label='Submit 2')
        
    if submitted1 and submitted2:
        # Only execute after the user clicks the button.
        # Verify that column name is valid and is numeric before plotting
        st.write("hello")
        if col1 in df.columns and is_numeric_dtype(df[col1]) and \
           col2 in df.columns and is_numeric_dtype(df[col2]):
            chart_data = df(['col1', 'col2'])

            st.scatter_chart(
                chart_data,
                x = 'col1',
                y = 'col2',
                size = 20,
                color = ['#FF0000', '#0000FF']
                )

            
        else:
            st.warning('Column name incorrect or not numeric. Try again.')
