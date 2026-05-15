import streamlit as st
import matplotlib.pyplot as plt
from data_loader import DataLoader
from data_cleaner import DataCleaner
from analyzer import Analyzer
import sqlite3
import pandas as pd
import airline_delay
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Cancellation Rate")

st.markdown("""
    <style>
    .stApp {
        background-color: #90d2cb;
        color: white;
    }

            .custom-text {
        font-size: 20px  !important;   /* Increase font size */
        color: #1f1f1f;
        font-weight: 500;
}   

     .block-container {
          #padding-top: 2rem;
          padding-left: 3rem;
          padding-right: 3rem;
     }

    h1, h2, h3 {
        color: ##00C4B4;
    }
    </style>
""", unsafe_allow_html=True)

#connect to DB
conn = sqlite3.connect("Airline_delay.db")
df = pd.read_sql("SELECT * FROM delays", conn)

#st.subheader("Raw Data")
#st.dataframe(df.head())


# Add filters (this is where Streamlit shines)
# years = sorted(df['year'].dropna().unique())
# selected_year = st.selectbox("Select Year", years)
# filtered_df = df[df['year'] == selected_year]

df['arr_cancelled'] = df['arr_cancelled'] / df['arr_flights'] *100

result = (
    df.groupby(['year', 'carrier_name'])['arr_cancelled']
    .mean()
    .reset_index()
    .sort_values(['year', 'arr_cancelled'])
    .head(10)
)

#df['year_not_2020'] = [2018, 2019, 2021, 2022, 2023, 2034]
df_filtered = df[df['year'] != 2020]

 #Pivot table
pivot = df.pivot_table(
    index='year',
    columns='carrier_name',
    values='arr_cancelled',
    aggfunc='mean'
)
pivot

pivot_2020 = df_filtered.pivot_table(
    index='year',
    columns='carrier_name',
    values='arr_cancelled',
    aggfunc='mean'
)


# fig = px.line(
#     result,
#     x='year',
#     y='arr_cancelled',
#     color='carrier_name',
#     markers=True,
#     title="Average Cancellation Rate by Airline Over Time"
# )


# fig = px.line(
#     pivot,
#     x=pivot.index,
#     y=pivot.columns,
#     title="Average Cancellation Rate by Airline Over Time"
# )
# st.plotly_chart(fig, use_container_width=True)



pivot_reset = pivot_2020.reset_index()
# fig = px.line(
#     pivot_reset,
#     x='year',
#     y=pivot_reset.columns[1:],  # all airline columns
#     title="Cancellation Rate by Airline"
# )
# st.plotly_chart(fig, use_container_width=True)



airlines = st.multiselect(
    "Select Airlines",
    pivot.columns,
    default=pivot.columns[:3]
)
filtered_pivot = pivot[airlines]
st.line_chart(filtered_pivot)




# fig = px.imshow(
#     pivot,
#     aspect="auto",
#     title="Cancellation Rate Heatmap"
# )
# st.plotly_chart(fig, use_container_width=True)

result_month = (
    df.groupby(['month', 'carrier_name'])['arr_cancelled']
    .mean()
    .reset_index()
    .sort_values(['month', 'arr_cancelled'])
    .head(10)
)

 
 #Pivot table
pivot2 = df_filtered.pivot_table(
    index='month',
    columns='carrier_name',
    values='arr_cancelled',
    aggfunc='mean'
)
pivot2

pivot2_reset = pivot2.reset_index()
fig = px.line(
    pivot2_reset,
    x='month',
    y=pivot_reset.columns[1:9],  # all airline columns
    title="Monthly Cancellation Rate by Airline"
)
st.plotly_chart(fig, use_container_width=True)


## last select airline
airlines2 = st.multiselect(
    "Select",
    pivot2.columns,
    default=pivot2.columns[:3]
)
filtered_pivot2 = pivot2[airlines2]
st.line_chart(filtered_pivot2)


st.markdown('<p class="custom-text"><br><br>Cancelations are higher during winter months'
'</p>', unsafe_allow_html=True)