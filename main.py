import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Load the data
df = pd.read_csv('economic-indicators.csv')

# Fill missing values
df.fillna(method='ffill', inplace=True)

# Set the style and color palette
sns.set(style="whitegrid")
palette = sns.color_palette("Set2")


# Function to plot passenger traffic over time
def plot_passenger_traffic_over_time(year_range):
    plt.figure(figsize=(10, 6))
    filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
    sns.lineplot(data=filtered_df, x='Year', y='logan_passengers', palette=palette)
    plt.title('Passenger Traffic at Logan Airport Over Time', fontsize=16, color='darkblue')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Number of Passengers', fontsize=14)
    plt.grid(True)
    st.pyplot(plt)


# Function to plot passenger traffic for a selected year
def plot_passenger_traffic_yearly(selected_year):
    yearly_data = df[df['Year'] == selected_year]
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=yearly_data, x='Month', y='logan_passengers', marker='o', palette=palette)
    plt.title(f'Passenger Traffic at Logan Airport in {selected_year}', fontsize=16, color='darkblue')
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Number of Passengers', fontsize=14)
    plt.grid(True)
    st.pyplot(plt)


# Function to plot the yearly data for a specific variable
def plot_yearly(variable, selected_year):
    yearly_data = df[df['Year'] == selected_year]
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=yearly_data, x='Month', y=variable, marker='o', palette=palette)
    plt.title(f'{variable.replace("_", " ").title()} in {selected_year}', fontsize=16, color='darkblue')
    plt.xlabel('Month', fontsize=14)
    plt.ylabel(variable.replace("_", " ").title(), fontsize=14)
    plt.grid(True)
    st.pyplot(plt)


# Function to plot the data over time for a specific variable
def plot_over_time(variable, year_range):
    plt.figure(figsize=(10, 6))
    filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
    sns.lineplot(data=filtered_df, x='Year', y=variable, palette=palette)
    plt.title(f'{variable.replace("_", " ").title()} Over Time', fontsize=16, color='darkblue')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel(variable.replace("_", " ").title(), fontsize=14)
    plt.grid(True)
    st.pyplot(plt)


# Function to plot a pie chart of passenger traffic distribution by year
def plot_pie_chart():
    plt.figure(figsize=(8, 8))
    yearly_data = df.groupby('Year')['logan_passengers'].sum()
    yearly_data.plot.pie(autopct='%1.1f%%', colors=palette, startangle=140)
    plt.title('Passenger Traffic Distribution by Year', fontsize=16, color='darkblue')
    plt.ylabel('')
    st.pyplot(plt)


# Function to create an animation of passenger traffic over time
def animate_passenger_traffic():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(df['Year'].min(), df['Year'].max())
    ax.set_ylim(df['logan_passengers'].min(), df['logan_passengers'].max())
    ax.set_title('Animated Passenger Traffic at Logan Airport Over Time', fontsize=16, color='darkblue')
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Number of Passengers', fontsize=14)
    line, = ax.plot([], [], lw=2, color='blue')

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        year_range = df['Year'].unique()[:frame + 1]
        filtered_df = df[df['Year'].isin(year_range)]
        line.set_data(filtered_df['Year'], filtered_df['logan_passengers'])
        return line,

    ani = FuncAnimation(fig, update, frames=np.arange(1, len(df['Year'].unique()) + 1), init_func=init, blit=True,
                        interval=500, repeat=False)
    st.pyplot(fig)


# Streamlit UI
st.title("Boston Economic Indicators Dashboard", anchor=None)

# Sidebar for year selection and range sliders
st.sidebar.title("Drill Down Panel")
year = st.sidebar.selectbox('Select Year', df['Year'].unique())
year_range = st.sidebar.slider('Select Year Range', int(df['Year'].min()), int(df['Year'].max()),
                               (int(df['Year'].min()), int(df['Year'].max())))

# Compartmentalized sections with expanders
with st.expander("Passenger Traffic at Logan Airport"):
    st.subheader("Over Time")
    plot_passenger_traffic_over_time(year_range)

    st.subheader(f'Yearly - {year}')
    plot_passenger_traffic_yearly(year)

    st.subheader("Passenger Traffic Distribution")
    plot_pie_chart()

    st.subheader("Animation Over Time")
    animate_passenger_traffic()

# Add similar sections for other variables
variables = ['hotel_occup_rate', 'hotel_avg_daily_rate', 'total_jobs', 'unemp_rate', 'labor_force_part_rate']
for variable in variables:
    with st.expander(variable.replace("_", " ").title()):
        st.subheader("Over Time")
        plot_over_time(variable, year_range)

        st.subheader(f'Yearly - {year}')
        plot_yearly(variable, year)
