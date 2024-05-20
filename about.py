import streamlit as st

import streamlit as st


def about_page():
    st.title('About')
    st.write('''
    **Data Source: Economic Indicators Legacy Portal**

    The dataset, curated by the Boston Planning and Redevelopment Authority (BPDA), formerly known as the Boston Redevelopment Authority (BRA), encompasses a range of economic indicators crucial for understanding the economic landscape of the City of Boston. These indicators cover various domains such as employment, housing, travel, and real estate development. The dataset spans monthly records from January 2013 to December 2019, offering insights into trends and patterns over this time period.

    Key Variables in the Dataset:
    - Employment Rate
    - Housing Prices
    - Toursim Data
    - Real Estate Development Projects

    [Link to Dataset](https://data.boston.gov/dataset/economic-indicators-legacy-portal)

    **Motivation:**

    This project aims to explore Boston's significance as a major global city and a key economic center. By analyzing economic data, we aim to uncover the factors, trends, patterns, and technologies driving Boston's economic growth. This analysis will not only offer practical suggestions but also strategic insights for decision-making, fostering sustainable economic development in Boston's planning and infrastructure.

    **References:**
    - [Boston Planning and Redevelopment Authority](http://www.bostonplans.org/research/)
    - [Boston Economic Indicators Dataset](https://data.boston.gov/dataset/economic-indicators-legacy-portal)
    - [Streamlit](https://streamlit.io/)
    - [Matplotlib](https://matplotlib.org/)
    ''')


