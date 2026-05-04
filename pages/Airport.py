import streamlit as st
import matplotlib.pyplot as plt
from data_loader import DataLoader
from data_cleaner import DataCleaner
from analyzer import Analyzer
import sqlite3
import pandas as pd
import airline_delay
import plotly.express as px

st.set_page_config(layout="centered")
st.title("Airport Bottleneck Analysis")

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


# Add filters (this is where Streamlit shines)
years = sorted(df['year'].dropna().unique())
selected_year = st.selectbox("Select Year", years)
filtered_df = df[df['year'] == selected_year]

####################################################################################################
# BOTTLE NECK ANALYSIS HERE
# from Analyzer class
analyzer = Analyzer(filtered_df)
bottlenecks = analyzer.airport_bottlenecks()
bottlenecks_name = analyzer.airport_bottlenecks2()

st.subheader("Airport Bottlenecks")
top_n = st.slider("Select number of airports", 5, 50, 10)
top_bottlenecks = bottlenecks_name.head(top_n)
st.dataframe(top_bottlenecks)


#plot above
# fig, ax = plt.subplots(figsize=(12,6))

# top_bottlenecks['avg_delay'].sort_values().plot(
#     kind='barh',
#     ax=ax
# )

# ax.set_title("Airports with Highest Average Delays")
# ax.set_xlabel("Average Delay (minutes)")

# st.pyplot(fig)



###################################
#slider
min_traffic = st.slider("Minimum Traffic", 0, int(bottlenecks['traffic'].max()), 100)
filtered = bottlenecks[bottlenecks['traffic'] >= min_traffic]


fig, ax = plt.subplots(figsize=(12,6))
filtered.sort_values(by='avg_delay').tail(10)['avg_delay'].plot(
    kind='bar',
    ax=ax
)
st.pyplot(fig)

# BOTTLE NECK ANALYSIS END
##
##################################################

# # Calculate quadrant thresholds
# x_mean = bottlenecks['traffic'].mean()
# y_mean = bottlenecks['avg_delay'].mean()

# fig, ax = plt.subplots(figsize=(10,8))

# # Scatter plot
# ax.scatter(
#     bottlenecks['traffic'],
#     bottlenecks['avg_delay'],
#     alpha=0.7
# )


# # Labels
# for airline in bottlenecks.index:
#     ax.text(
#         bottlenecks.loc[airline, 'traffic'],
#         bottlenecks.loc[airline, 'avg_delay'],
#         airline,
#         fontsize=8
#     )


# # Add quadrant lines
# ax.axvline(x=x_mean, color='red', linestyle='--')
# ax.axhline(y=y_mean, color='red', linestyle='--')

# # Labels
# ax.set_xlabel("Traffic (Number of Flights)")
# ax.set_ylabel("Average Delay")
# ax.set_title("Airport Bottlenecks: Traffic vs Delay (Quadrant View)")

# # Optional: quadrant labels
# ax.text(x_mean * 0.05, y_mean * 4.5, "Low Traffic / High Delay", fontsize=10)
# ax.text(x_mean * 4.5, y_mean * 1.5, "High Traffic / High Delay", fontsize=10)
# ax.text(x_mean * 0.05, y_mean * 0.5, "Low Traffic / Low Delay", fontsize=10)
# ax.text(x_mean * 4.5, y_mean * 0.5, "High Traffic / Low Delay", fontsize=10)

# st.pyplot(fig)




##################################################

# Calculate quadrant thresholds
# x_mean = filtered['traffic'].mean()
# y_mean = filtered['avg_delay'].mean()

x_mean = bottlenecks['traffic'].mean()
y_mean = bottlenecks['avg_delay'].mean()

fig, ax = plt.subplots(figsize=(10,8))

# Scatter plot
ax.scatter(
    filtered['traffic'],
    filtered['avg_delay'],
    alpha=0.7
)


# Labels
for airline in filtered.index:
    ax.text(
        filtered.loc[airline, 'traffic'],
        filtered.loc[airline, 'avg_delay'],
        airline,
        fontsize=8
    )


# ax.set_xlim(filtered['traffic'].min(), filtered['traffic'].max())
# ax.set_ylim(filtered['avg_delay'].min(), filtered['avg_delay'].max())


# Add quadrant lines
ax.axvline(x=x_mean, color='red', linestyle='--')
ax.axhline(y=y_mean, color='red', linestyle='--')

# Labels
ax.set_xlabel("Traffic (Number of Flights)")
ax.set_ylabel("Average Delay")
ax.set_title("Airport Bottlenecks: Traffic vs Delay (Quadrant View)")

# Optional: quadrant labels
# 
ax.text(x_mean * 1.5, y_mean * 1.5, "Above Average Delay", fontsize=14, color='red')

st.pyplot(fig)


