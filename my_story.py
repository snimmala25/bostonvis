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



# Main function
def my_story_page():
    st.title('My Story')
    st.write("___")
    # Load the data
    data = load_data()

    # Normalize data for plotting
    normalized_df = data.copy()
    normalized_df.iloc[:, 1:] = (data.iloc[:, 1:] - data.iloc[:, 1:].mean()) / data.iloc[:, 1:].std()

    # Plot key economic indicators
    plot_key_indicators(normalized_df)



    # Dropdown to select exact year
    selected_year = st.sidebar.selectbox('Select Year', data['Year'].unique())
    monthly_data = data[data['Year'] == selected_year]
    st.sidebar.dataframe(monthly_data)

    st.image("laborstack.png")
    st.write("___")
    st.title('Exploring Boston\'s Economic Story')
    st.write("___")
    # Write narrative
    st.header("Unlocking Boston's Economic Potential")
    st.markdown(
       ("""Boston: Where Economic Resilience and Community Flourish""")
    )
    st.write("___")
    st.subheader("Thriving Tourism Sector")
    st.write("___")
    st.markdown(
        """
        The tourism sector in Boston has witnessed remarkable growth, as evidenced by the surge in hotel occupancy rates 
        and international passenger traffic at Logan Airport. Months like June, July, and August typically experience 
        peak tourism activity, marked by a surge in visitors exploring the city's rich history, cultural landmarks, 
        and vibrant neighborhoods. Conversely, December sees a dip in hotel occupancy, reflecting the seasonal nature 
        of tourism in Boston.
        """
    )
    st.write("___")
    st.subheader("Fluctuating Real Estate Market")
    st.write("___")
    st.markdown(
        """
        Boston's real estate market presents a mixed picture, with a steady decrease in affordable housing permits 
        juxtaposed with overall economic growth. While the city's economy continues to thrive, the decline in 
        affordable housing permits may pose challenges for residents seeking homeownership. This underscores the 
        importance of addressing housing affordability as a key aspect of Boston's economic development efforts.
        """
    )
    st.write("___")
    st.subheader("Dynamic Labor Market")
    st.write("___")
    st.markdown(
        """
        Boston's labor market is dynamic and robust, with steady job creation and increasing labor force participation 
        rates. The decline in the unemployment rate underscores the city's ability to provide ample employment opportunities 
        for its residents. The months of June, July, and August coincide with increased job opportunities, driven by 
        seasonal industries such as tourism, hospitality, and outdoor recreation.
        """
    )
    st.write("___")
    st.subheader("A Narrative of Progress")
    st.title("Overall Conclusion")

    # Introduction
    st.header("Economic Prosperity and Tourism Flourish")

    # Paragraph 1
    st.write(
        "Our analysis indicates a robust and thriving economy in the Boston area. Despite fluctuations in certain sectors, key economic indicators such as total jobs, labor force participation rate, and Hotel occupancy show an overall upward trend over the years. This sustained growth reflects the resilience of the local economy and its ability to adapt to changing market conditions.")

    # Paragraph 2
    st.write(
        "Additionally, the tourism industry in Boston is experiencing a period of unprecedented growth. International passenger traffic at Logan Airport has seen a significant increase, indicating a rising interest in Boston as a travel destination. The surge in tourism not only boosts the local economy through increased spending but also enhances the city's reputation as a vibrant cultural hub.")

    # Paragraph 3
    st.write(
        "While the real estate market may face challenges such as decreasing median house prices and permits for affordable housing, it is important to note that these fluctuations are part of a broader economic cycle. Moreover, some data points showing zero values may be attributed to data insufficiency rather than actual trends. Despite these challenges, the overall economic landscape remains promising.")

    # Conclusion
    st.write(
        "In summary, Boston's economy is thriving, driven by strong job growth, increasing tourism, and a dynamic real estate market. As we move forward, continued investment in key sectors and strategic planning will be essential to sustain this positive momentum and ensure long-term prosperity for the city and its residents.")

if __name__ == "__main__":
    my_story_page()
