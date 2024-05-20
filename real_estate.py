import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def real_estate_page():
    # Load real estate data
    real_estate_df = pd.read_csv('economic-indicators.csv')

    # Fill missing values
    real_estate_df.fillna(method='ffill', inplace=True)

    # Set the style and color palette
    sns.set(style="whitegrid")
    palette = sns.color_palette("Set2")

    # Streamlit metric code for real estate
    col1, col2, col3 = st.columns(3)

    # Get the selected year from the drill-down panel
    selected_year = st.sidebar.selectbox('Select Year Real Estate Metrics', real_estate_df['Year'].unique(),
                                         key='select_year_real_estate_metrics')


    # Title
    st.title("Understanding the Real Estate Market Dynamics")


    # Analysis
    st.subheader("Overall Trends")
    st.write(
        "Our analysis reveals a consistent pattern of decline across various indicators in the real estate market.")

    ## Subheading: Key Findings
    st.subheader("Key Findings")
    st.write("___")
    st.write("some might show 0 due to data inconsistency by the govt")
    st.write("___")
    ### Median House Price
    st.write("**Median House Price:**")
    st.write("The median house price has shown a notable decrease, indicating a downward trend in property values, some might show due to data inconsistency by the government.")

    ### House Sales
    st.write("**House Sales:**")
    st.write(
        "There has been a decrease in house sales, which aligns with the decline in median house price and suggests a slowdown in the real estate market.")

    ### Affordable Housing Permits
    st.write("**Affordable Housing Permits:**")
    st.write(
        "Permits for affordable housing construction have also decreased, highlighting a potential lack of investment in this segment and further contributing to the market slowdown.")

    ### Other Factors
    st.write("**Other Factors:**")
    st.write(
        "Additionally, various other factors such as pipeline units, total development costs, square footage, and construction jobs have shown a downward trend, indicating an overall decline in real estate activity.")

    # Conclusion
    st.header("Conclusion")
    st.write(
        "In conclusion, our analysis paints a picture of a declining real estate market characterized by decreasing median house prices, reduced sales, and fewer permits for affordable housing construction. These trends suggest a challenging environment for both buyers and developers and underscore the importance of strategic planning and adaptation to navigate the complexities of the current real estate landscape.")

    # Calculate metrics based on the selected year
    year_data = real_estate_df[real_estate_df['Year'] == selected_year]
    #pipeline_unit_value = year_data['pipeline_unit'].sum()
    #pipeline_total_dev_cost_value = year_data['pipeline_total_dev_cost'].sum()
    #pipeline_sqft_value = year_data['pipeline_sqft'].sum()
    #pipeline_const_jobs_value = year_data['pipeline_const_jobs'].sum()
    #foreclosure_pet_value = year_data['foreclosure_pet'].sum()
    #foreclosure_deeds_value = year_data['foreclosure_deeds'].sum()
    med_housing_price_value = year_data['med_housing_price'].mean()
    housing_sales_vol_value = year_data['housing_sales_vol'].sum()
    new_housing_const_permits_value = year_data['new_housing_const_permits'].sum()
    new_affordable_housing_permits_value = year_data['new-affordable_housing_permits'].sum()

    # Display metrics
    #col1.metric("Pipeline Units", f"{pipeline_unit_value}", "")
   # col2.metric("Total Development Cost", f"${pipeline_total_dev_cost_value:,.2f}", "")
    #col3.metric("Pipeline Square Feet", f"{pipeline_sqft_value}", "")

    #col1.metric("Pipeline Construction Jobs", f"{pipeline_const_jobs_value}", "")
    #col2.metric("Foreclosure Petitions", f"{foreclosure_pet_value}", "")
    #col3.metric("Foreclosure Deeds", f"{foreclosure_deeds_value}", "")

    col1.metric("Median Housing Price", f"${med_housing_price_value:,.2f}", "")
    col2.metric("Housing Sales Volume", f"{housing_sales_vol_value}", "")
    col3.metric("New Housing Construction Permits", f"{new_housing_const_permits_value}", "")

    col1.metric("New Affordable Housing Permits", f"{new_affordable_housing_permits_value}", "")

    # Function to plot the data over time for a specific variable
    def plot_over_time(variable, year_range):
        plt.figure(figsize=(10, 6))
        filtered_df = real_estate_df[(real_estate_df['Year'] >= year_range[0]) & (real_estate_df['Year'] <= year_range[1])]
        sns.lineplot(data=filtered_df, x='Year', y=variable, palette=palette)
        plt.title(f'{variable.replace("_", " ").title()} Over Time', fontsize=16, color='darkblue')
        plt.xlabel('Year', fontsize=14)
        plt.ylabel(variable.replace("_", " ").title(), fontsize=14)
        plt.grid(True)
        st.pyplot(plt)

    # Compartmentalized sections with expanders

    with st.expander("Median Housing Price Over Time"):
        st.subheader("Median Housing Price Over Time")
        plot_over_time('med_housing_price', (int(real_estate_df['Year'].min()), int(real_estate_df['Year'].max())))

    with st.expander("Housing Sales Volume Over Time"):
        st.subheader("Housing Sales Volume Over Time")
        plot_over_time('housing_sales_vol', (int(real_estate_df['Year'].min()), int(real_estate_df['Year'].max())))

    with st.expander("New Housing Construction Permits Over Time"):
        st.subheader("New Housing Construction Permits Over Time")
        plot_over_time('new_housing_const_permits', (int(real_estate_df['Year'].min()), int(real_estate_df['Year'].max())))

    with st.expander("New Affordable Housing Permits Over Time"):
        st.subheader("New Affordable Housing Permits Over Time")
        plot_over_time('new-affordable_housing_permits', (int(real_estate_df['Year'].min()), int(real_estate_df['Year'].max())))

# Run the function
real_estate_page()
