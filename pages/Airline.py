import streamlit as st
import matplotlib.pyplot as plt
from data_loader import DataLoader
from data_cleaner import DataCleaner
from analyzer import Analyzer
import sqlite3
import pandas as pd
import airline_delay
import plotly.express as px

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
        color: #088f8f;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(layout="centered")
st.title("Airline Analysis")

#connect to DB
conn = sqlite3.connect("Airline_delay.db")
df = pd.read_sql("SELECT * FROM delays", conn)


# Add filters (this is where Streamlit shines)
years = sorted(df['year'].dropna().unique())
selected_year = st.selectbox("Select Year", years)
filtered_df = df[df['year'] == selected_year]

####################################################################################################
##################################################
#airline_reliability

analyzer = Analyzer(filtered_df)
reliability = analyzer.airline_reliability()


st.subheader("Airline Reliability: Which airline is most reliable")
top_n = st.slider("Number of airlines", 5, 20, 10)
top_airlines = reliability.head(top_n)
st.dataframe(top_airlines)
# metric = st.selectbox(
#     "Sort by",
#     ["arr_cancelled", "arr_delay", "dep_delay"]
# )
# top_n = st.slider("Number of airlines", 5, 20, 10)
# sorted_df = reliability.sort_values(by=metric, ascending=True)
# top_airlines = sorted_df.head(top_n)
# st.dataframe(top_airlines)



fig, ax = plt.subplots(figsize=(12,10))
top_airlines['avg_delay'].sort_values().plot(
    kind='barh',
    ax=ax
)
ax.set_title("Airline Delay (Per minute)")
ax.set_xlabel("Delays")
st.pyplot(fig)



#scatter plot
# fig, ax = plt.subplots(figsize=(12,8))
# ax.scatter(
#     reliability['delay_rate'],
#     reliability['avg_delay']
# )
# for airline in reliability.index:
#     ax.text(
#         reliability.loc[airline, 'delay_rate'],
#         reliability.loc[airline, 'avg_delay'],
#         airline,
#         fontsize=10
#     )
# ax.set_xlabel("Delay Rate")
# ax.set_ylabel("Average Delay (minutes)")
# ax.set_title("Airline Reliability: Delay Rate vs Avg Delay")

# st.pyplot(fig)


# quandrant
fig, ax = plt.subplots(figsize=(12,10))

# Scatter plot
ax.scatter(
    reliability['delay_rate'],
    reliability['avg_delay']
)

# Labels
for airline in reliability.index:
    ax.text(
        reliability.loc[airline, 'delay_rate'],
        reliability.loc[airline, 'avg_delay'],
        airline,
        fontsize=8
    )

# 👉 Calculate quadrant lines
x_mean = reliability['delay_rate'].mean()
y_mean = reliability['avg_delay'].mean()



# 👉 Draw quadrant lines
ax.axvline(x=x_mean, linestyle='--')
ax.axhline(y=y_mean, linestyle='--')

# Titles and labels
ax.set_xlabel("Delay Rate")
ax.set_ylabel("Average Delay (minutes)")
ax.set_title("Airline Reliability: Quadrant Analysis")

#ax.text(0.05, y_mean + 50, "Rare but Severe", fontsize=12)
ax.text(x_mean * 1.5, y_mean * 1.5, "Worst", fontsize=14, color='red')
ax.text(x_mean * 0.1, y_mean * 1.5, "Infrequent/Large", fontsize=14, color='blue')
ax.text(x_mean * 0.1, y_mean * 0.8, "Best", fontsize=14, color='green')
ax.text(x_mean * 1.5, y_mean * 0.8, "Frequent/Small Delays", fontsize=14, color='green')

st.pyplot(fig)