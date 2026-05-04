import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import airline_delay
import plotly.express as px

from analyzer import Analyzer

st.markdown("""
    <style>
    .stApp {
        background-color: #b3e0dc;
        color: white;
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
years = sorted(df['year'].dropna().unique())
selected_year = st.selectbox("Select Year", years)
filtered_df = df[df['year'] == selected_year]

# Airline performance chart
import matplotlib.pyplot as plt

airline_perf = (
    filtered_df.groupby('carrier_name')['arr_delay']
    .mean()
    .sort_values()
    .head(20)
)
########################################
########################################

airline_factor = filtered_df.groupby('carrier_name')[[
    'carrier_delay',
    'weather_delay',
    'nas_delay',
    'security_delay',
    'late_aircraft_delay'
]].mean().nlargest(10, 'carrier_delay')

df_long = airline_factor.reset_index().melt(
    id_vars='carrier_name',
    var_name='delay_type',
    value_name='delay_value'
)

#based on month
month_factor = filtered_df.groupby('month')[[
    'carrier_delay',
    'weather_delay',
    'nas_delay',
    'security_delay',
    'late_aircraft_delay'
]].mean()

df_plot = month_factor.reset_index()


fig, ax = plt.subplots()




# fig = px.line(
#     df_plot,
#     x='month',
#     y=[
#         'carrier_delay',
#         'weather_delay',
#         'nas_delay',
#         'security_delay',
#         'late_aircraft_delay'
#     ],
#     markers=True,
#     title="Delay Factors by Month"
# )

# st.plotly_chart(fig, use_container_width=True)


# causes of delays
delay_factors = filtered_df[[
    'carrier_delay',
    'weather_delay',
    'nas_delay',
    'security_delay',
    'late_aircraft_delay'
]].sum()

# causes of cancellations
cancelled = filtered_df[[
    'arr_cancelled',
]].sum()

delay_factors.plot( kind='pie',
    autopct='%1.1f%%',   # shows percentages
    startangle=90,       # rotates for better view
    ax=ax
)
ax.set_ylabel("")  # removes default "ylabel"
ax.set_title("Delay Causes Contribution")
st.pyplot(fig)




st.line_chart(month_factor)

##### PLOT
# fig = px.area(
#     df_plot,
#     x='month',
#     y=[
#         'carrier_delay',
#         'weather_delay',
#         'nas_delay',
#         'security_delay',
#         'late_aircraft_delay'
#     ],
#     title="Monthly Delay Composition"
# )
# st.plotly_chart(fig, use_container_width=True)




options = st.multiselect(
    "Select delay types",
    month_factor.columns,
    default=list(month_factor.columns)
)
df_plot = month_factor.reset_index()
fig = px.line(df_plot, x='month', y=options, markers=True)
st.plotly_chart(fig, use_container_width=True)
#########################



state_delay = (
    filtered_df.groupby('state')['arr_delay']
    .mean()
    .sort_values(ascending=False)
    .head(15)
)







# fig, ax = plt.subplots()
# delay_factors.sort_values().plot(kind='barh', ax=ax)
# ax.set_title("Delay Causes Contribution")
# st.pyplot(fig)



# fig, ax = plt.subplots()
# airline_perf.sort_values().plot(kind='barh', ax=ax)
# ax.set_title("Delay Causes Contribution")
# st.pyplot(fig)



###### CANCELLATION

# result = (
#     df.groupby(['year', 'carrier_name'])['arr_cancelled']
#     .mean()
#     .reset_index()
#     .sort_values(['year', 'arr_cancelled'])
# )
 
# fig = px.line(
#     result,
#     x='year',
#     y='arr_cancelled',
#     color='carrier_name',
#     markers=True,
#     title="Average Cancellation Rate by Airline Over Time"
# )



fig = px.bar(
    df_long,
    x='carrier_name',
    y='delay_value',
    color='delay_type',
    barmode='group',
    title="Delay Factors by Airline"
)


st.plotly_chart(fig, use_container_width=True)


# #### EXTRA - stack bar
# fig = px.bar(
#     df_long,
#     x='carrier_name',
#     y='delay_value',
#     color='delay_type',
#     title="Total Delay Contribution by Airline"
# )

# st.plotly_chart(fig, use_container_width=True)



#### EXTRA PLOT 
# fig = px.bar(
#     airline_factor.reset_index(),
#     x='carrier_name',
#     y='carrier_delay',
#     title="Top 10 Airlines by Carrier Delay"
# )

# st.plotly_chart(fig, use_container_width=True)