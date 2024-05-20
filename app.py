import streamlit as st
from home import home_page
from about import about_page
from tourism import tourism_page
from jobs import jobs_page
from real_estate import real_estate_page
from my_story import my_story_page

# Set up sidebar
st.sidebar.title('Boston Visualizations')
st.sidebar.image('https://cdn5.vectorstock.com/i/1000x1000/88/59/logo-for-boston-vector-31288859.jpg', caption='Boston Map')

# Navigation
page = st.sidebar.radio('Navigation', ['My Story', 'About', 'Tourism', 'Jobs', 'Real Estate'])

# Main content
if page == 'Home':
    home_page()

elif page == 'About':
    about_page()

elif page == 'Tourism':
    tourism_page()

elif page == 'Jobs':
    jobs_page()

elif page == 'Real Estate':
    real_estate_page()

elif page == 'My Story':
    my_story_page()



