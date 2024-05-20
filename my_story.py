import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    data = pd.read_csv("economic-indicators.csv")
    return data

# Function to plot key economic indicators over time
def plot_key_indicators(data):
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.lineplot(data=data, x='Year', y='logan_passengers', label='Logan Passengers', ax=ax)
    sns.lineplot(data=data, x='Year', y='hotel_occup_rate', label='Hotel Occupancy Rate', ax=ax)
    sns.lineplot(data=data, x='Year', y='total_jobs', label='Total Jobs', ax=ax)
    sns.lineplot(data=data, x='Year', y='unemp_rate', label='Unemployment Rate', ax=ax)
    ax.set_title('Key Economic Indicators in Boston Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Normalized Values')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Function to plot monthly data for the selected year


# Main function
def my_story_page():
    st.title('My Story')

    # Load the data
    data = load_data()

    # Normalize data for plotting
    normalized_df = data.copy()
    normalized_df.iloc[:, 1:] = (data.iloc[:, 1:] - data.iloc[:, 1:].mean()) / data.iloc[:, 1:].std()

    # Plot key economic indicators
    plot_key_indicators(normalized_df)

    # Dropdown to select exact year
    selected_year = st.sidebar.selectbox('Select Year', data['Year'].unique())


if __name__ == "__main__":
    my_story_page()
