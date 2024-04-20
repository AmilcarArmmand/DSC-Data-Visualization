import streamlit as st
import pandas as pd
from pandas.api.types import is_numeric_dtype
from io import StringIO
import matplotlib.pyplot as plt

st.title('Scatter-plot renderer')

uploaded_file = st.file_uploader("Choose a file")
# Upload the file after the user makes a selection.
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # display the dataframe in the app
    st.dataframe(df)

    with st.form(key='columns_in_form'):
        cols = st.columns(2)
        col1 = st.text_input("Type here")
        col2 = st.text_input("Type here", key = "second")
        
        submitted = st.form_submit_button(label='Submit')

        
        if submitted:
            # Only execute after the user clicks the button.
            # Verify that column name is valid and is numeric before plotting
            if col1 in df.columns and is_numeric_dtype(df[col1]) and col2 in df.columns and is_numeric_dtype(df[col2]):
                chart_data = df.loc[:,[col1, col2]]

                st.scatter_chart(
                    chart_data,
                    x = col1,
                    y = col2,
                    size = 20
                    )
            else:
                st.warning('Column name incorrect or not numeric. Try again.')
