import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def jobs_page():
    df = pd.read_csv('economic-indicators.csv')

    # Fill missing values
    df.fillna(method='ffill', inplace=True)

    # Set the style and color palette
    sns.set(style="whitegrid")
    palette = sns.color_palette("Set2")

    # Streamlit metric code for economic indicators
    col1, col2, col3 = st.columns(3)

    # Get the selected year from the sidebar
    selected_year = st.sidebar.selectbox('Select Year Metrics', df['Year'].unique(), key='select_year_metrics')

    # Calculate metrics based on the selected year
    year_data = df[df['Year'] == selected_year]
    total_jobs_value = year_data['total_jobs'].sum()
    unemployment_rate_value = year_data['unemp_rate'].mean()
    labor_force_participation_value = year_data['labor_force_part_rate'].mean()

    # Display metricsr
    col1.metric("Total Jobs", f"{total_jobs_value}", "jobs")
    col2.metric("Unemployment Rate", f"{unemployment_rate_value:.2f}%", "-rate")
    col3.metric("Labor Force Participation", f"{labor_force_participation_value:.2f}%", "rate")
    st.write("___")
    st.title("Analyzing Job Market in Boston")
    st.write("___")

    # Introduction


    ## Subheading: Job Growth and Unemployment Trends
    st.subheader("Job Growth and Unemployment Trends")
    st.write("We observe a consistent trend of job growth and declining unemployment rates during the holiday season.")

    ## Subheading: Reasons Behind the Trend
    st.subheader("Reasons Behind the Trend")

    ### Sub-subheading: Increased Economic Activity
    st.write("Increased Economic Activity")
    st.write(
        "The holiday season brings about heightened economic activity, leading to increased demand for goods and services.")

    ### Sub-subheading: Year-End Projects and Budgets
    st.write("Year-End Projects and Budgets")
    st.write(
        "Companies often finalize projects, meet deadlines, and allocate remaining budgets, resulting in increased hiring.")

    ### Sub-subheading: Seasonal Events and Social Gatherings
    st.write("Seasonal Events and Social Gatherings")
    st.write(
        "Events like holiday parties and increased social gatherings drive demand for services, leading to more job opportunities.")

    # Conclusion
    st.header("Conclusion")
    st.write(
        "The holiday season, particularly the months of November and December, witnesses a surge in job creation and a decline in unemployment rates. This trend is fueled by increased economic activity, year-end projects, and seasonal events.")

    # Sidebar for year selection and range sliders
    year_range = st.sidebar.slider('Select Year Range', int(df['Year'].min()), int(df['Year'].max()),
                                   (int(df['Year'].min()), int(df['Year'].max())))

    # Function to plot jobs over time
    def plot_jobs_over_time(year_range):
        plt.figure(figsize=(10, 6))
        filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
        sns.lineplot(data=filtered_df, x='Year', y='total_jobs', palette=palette)
        plt.title('Total Jobs Over Time', fontsize=16, color='darkblue')
        plt.xlabel('Year', fontsize=14)
        plt.ylabel('Total Jobs', fontsize=14)
        plt.grid(True)
        st.pyplot(plt)

    # Function to plot unemployment rate over time
    def plot_unemployment_over_time(year_range):
        plt.figure(figsize=(10, 6))
        filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
        sns.lineplot(data=filtered_df, x='Year', y='unemp_rate', palette=palette)
        plt.title('Unemployment Rate Over Time', fontsize=16, color='darkblue')
        plt.xlabel('Year', fontsize=14)
        plt.ylabel('Unemployment Rate (%)', fontsize=14)
        plt.grid(True)
        st.pyplot(plt)

    # Function to plot labor force participation rate over time
    def plot_labor_force_participation_over_time(year_range):
        plt.figure(figsize=(10, 6))
        filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
        sns.lineplot(data=filtered_df, x='Year', y='labor_force_part_rate', palette=palette)
        plt.title('Labor Force Participation Rate Over Time', fontsize=16, color='darkblue')
        plt.xlabel('Year', fontsize=14)
        plt.ylabel('Labor Force Participation Rate (%)', fontsize=14)
        plt.grid(True)
        st.pyplot(plt)

    # Function to plot yearly data for a specific variable
    def plot_yearly(variable, selected_year):
        yearly_data = df[df['Year'] == selected_year]
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=yearly_data, x='Month', y=variable, marker='o', palette=palette)
        plt.title(f'{variable.replace("_", " ").title()} in {selected_year}', fontsize=16, color='darkblue')
        plt.xlabel('Month', fontsize=14)
        plt.ylabel(variable.replace("_", " ").title(), fontsize=14)
        plt.grid(True)
        st.pyplot(plt)

    # Compartmentalized sections with expanders
    with st.expander("Total Jobs"):
        st.subheader("Metrics")
        st.write("Total Jobs:", total_jobs_value)

        st.subheader("Over Time")
        plot_jobs_over_time(year_range)

        st.subheader(f'Yearly - {selected_year}')
        plot_yearly('total_jobs', selected_year)

    with st.expander("Unemployment Rate"):
        st.subheader("Metrics")
        st.write("Unemployment Rate:", f"{unemployment_rate_value:.2f}%")

        st.subheader("Over Time")
        plot_unemployment_over_time(year_range)

        st.subheader(f'Yearly - {selected_year}')
        plot_yearly('unemp_rate', selected_year)

    with st.expander("Labor Force Participation Rate"):
        st.subheader("Metrics")
        st.write("Labor Force Participation Rate:", f"{labor_force_participation_value:.2f}%")

        st.subheader("Over Time")
        plot_labor_force_participation_over_time(year_range)

        st.subheader(f'Yearly - {selected_year}')
        plot_yearly('labor_force_part_rate', selected_year)

# Run the function
jobs_page()
