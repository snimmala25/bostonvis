import json
import streamlit as st
from streamlit_echarts import st_echarts

# Define the JSON data structure
data = {
    "name": "BOSTON ECONOMIC INDICATORS",
    "children": [
        {
            "name": "TOURISM",
            "children": [
                { "name": "Total Flight Passengers" },
                { "name": "Total International Flights" },
                { "name": "Total Hotel Occupancy" },
                { "name": "Avg Hotel Rate" }
            ]
        },
        {
            "name": "JOB MARKET",
            "children": [
                { "name": "Total Unemployed" },
                { "name": "Total Jobs" },
                { "name": "Total Labor Force Part Rate" }
            ]
        },
        {
            "name": "REALESTATE",
            "children": [
                { "name": "Total Housing" },
                { "name": "Total Affordable Housings" }
            ]
        }
    ]
}

# Optionally, manipulate the data to set 'collapsed' attribute
for idx, _ in enumerate(data["children"]):
    data["children"][idx]["collapsed"] = idx % 2 == 0

# Define ECharts option with customizations
option = {
    "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
    "series": [
        {
            "type": "tree",
            "data": [data],
            "top": "1%",
            "left": "7%",
            "bottom": "1%",
            "right": "20%",
            "symbolSize": 7,
            "label": {
                "position": "left",
                "verticalAlign": "middle",
                "align": "right",
                "fontSize": 14,
                "color": "darkgreen",
            },
            "itemStyle": {
                "color": "darkgreen",
                "borderColor": "darkgreen",
            },
            "leaves": {
                "label": {
                    "position": "right",
                    "verticalAlign": "middle",
                    "align": "left",
                    "fontSize": 14,
                    "color": "darkgreen",
                }
            },
            "emphasis": {"focus": "descendant"},
            "expandAndCollapse": True,
            "animationDuration": 550,
            "animationDurationUpdate": 750,
        }
    ],
}

# Add a heading
st.title("Boston Economic Indicators Tree Chart")
st.subheader("Click on the data to get more info")

# Display the chart in Streamlit
st_echarts(option, height="500px")
