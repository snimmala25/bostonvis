import streamlit as st

def year_selection():
    st.sidebar.title('Year Selection')
    year = st.sidebar.slider('Select Year', 2012, 2019, (2012, 2019))
    st.sidebar.write(f'Selected Year Range: {year[0]} - {year[1]}')

