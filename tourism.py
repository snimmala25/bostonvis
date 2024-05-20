import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def tourism_page():
    st.write("___")
    st.title("Analysing tourism in Boston")
    st.write("___")
    st.write(
        "Hotel occupancy and international passengers are higher in the month of (June, July, August) compared to December:")

    explanation = """
       1. **Summer Vacation**: Families often plan vacations during the summer months, leading to increased travel and demand for hotel accommodations.
       2. **Tourist Season**: Many tourist destinations experience peak seasons during the summer due to favorable weather conditions and attractions.
       3. **Special Events**: Summer months often coincide with events, festivals, and outdoor activities that attract tourists.
       4. **School Holidays**: School breaks in summer encourage family travel, contributing to higher occupancy rates.
       """

    st.markdown(explanation, unsafe_allow_html=True)
    df = pd.read_csv('economic-indicators.csv')
    st.write(
        "As Per the Below Graphs we can see there is a steady increase of hotel occupancy and international passengers which conveys there is stead increase in toursim which thereby convery that the economy is growing")

    # Fill missing values
    df.fillna(method='ffill', inplace=True)

    # Set the style and color palette
    sns.set(style="whitegrid")
    palette = sns.color_palette("Set2")

    # Streamlit metric code for economic indicators
    col1, col2, col3 = st.columns(3)

    # Get the selected year from the drill-down panel
    selected_year = st.sidebar.selectbox('Select Year', df['Year'].unique(), key='select_year_tourism_metrics')

    # Calculate metrics based on the selected year
    year_data = df[df['Year'] == selected_year]
    total_passengers_value = year_data['logan_passengers'].sum()
    total_intl_flights_value = year_data['logan_intl_flights'].sum()
    avg_hotel_occupancy_value = year_data['hotel_occup_rate'].mean()

    # Display metrics
    col1.metric("Total Passengers", f"{total_passengers_value}", "passengers")
    col2.metric("Total Intl Flights", f"{total_intl_flights_value}", "flights")
    col3.metric("Avg Hotel Occupancy", f"{avg_hotel_occupancy_value:.2f}%", "rate")

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

    # Function to plot international flights for a selected year
    def plot_intl_flights_yearly(selected_year):
        yearly_data = df[df['Year'] == selected_year]
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=yearly_data, x='Month', y='logan_intl_flights', marker='o', palette=palette)
        plt.title(f'International Flights at Logan Airport in {selected_year}', fontsize=16, color='darkblue')
        plt.xlabel('Month', fontsize=14)
        plt.ylabel('Number of International Flights', fontsize=14)
        plt.grid(True)
        st.pyplot(plt)

    # Function to plot hotel occupancy rate
    def plot_hotel_occupancy():
        plt.figure(figsize=(12, 6))
        pivot_df = df.pivot(index="Year", columns="Month", values="hotel_occup_rate")
        sns.heatmap(pivot_df, cmap="YlGnBu", annot=True, fmt=".1f")
        plt.title('Hotel Occupancy Rate in Boston', fontsize=16, color='darkblue')
        plt.xlabel('Month', fontsize=14)
        plt.ylabel('Year', fontsize=14)
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

    # Compartmentalized sections with expanders
    with st.expander("Passenger Traffic at Logan Airport"):
        st.subheader("Over Time")
        plot_passenger_traffic_over_time(year_range=(int(df['Year'].min()), int(df['Year'].max())))

        st.subheader(f'Yearly - {selected_year}')
        plot_passenger_traffic_yearly(selected_year)

    with st.expander("International Flights at Logan Airport"):
        st.subheader(f'Yearly - {selected_year}')
        plot_intl_flights_yearly(selected_year)

    with st.expander("Hotel Occupancy Rate in Boston"):
        st.subheader("Occupancy Rate Over Time")
        plot_hotel_occupancy()

    variables = ['hotel_avg_daily_rate']
    for variable in variables:
        with st.expander(variable.replace("_", " ").title()):
            st.subheader("Over Time")
            plot_over_time(variable, year_range=(int(df['Year'].min()), int(df['Year'].max())))

            st.subheader(f'Yearly - {selected_year}')
            plot_yearly(variable, selected_year)


# Run the function
tourism_page()
