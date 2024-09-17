import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

DATA_DIMENSIONS = (20,3)
DATA_COLUMNS = ['a','b','c']

st.title('Plots and Media Files')
st.subheader('Human Computer Interaction')

basicPlot = st.checkbox('Basic Plots')
if basicPlot:
    df = pd.DataFrame(np.random.rand(*DATA_DIMENSIONS), columns=DATA_COLUMNS)
    st.dataframe(df)
    st.line_chart(df)

personalInfo = st.checkbox('Personal Information')
if personalInfo:
    p_info = {
        'Name': ['Greg','Alice','Leo','Rebecca','David'],
        'Height': [184,156,169,172,180],
        'Weight': [110,89,68,75,91]
    }
    df2 = pd.DataFrame(p_info)
    st.dataframe(df2)
    avg_weight = df2['Weight'].mean()
    st.write(f'The average weight is: {avg_weight}')

col1,col2 = st.columns(2)
with col1:
    st.write('To be completed next week')
with col2:
    st.write('Have a great weekend!')
    st.balloons()