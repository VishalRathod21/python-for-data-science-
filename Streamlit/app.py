import streamlit as st
import pandas as pd
import numpy as np

### Title of Aplication
st.title('My First Streamlit App')


## Display a simple text 
st.write('Here is a simple text')   

## Display a simple data frame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

## Display a data frame

st.write("Here is a simple data frame")
st.write(df)

## create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
  
st.line_chart(chart_data)