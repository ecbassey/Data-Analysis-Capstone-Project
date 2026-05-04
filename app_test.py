import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import airline_delay

#from data_loader import DataLoader
#from data_cleaner import DataCleaner
from analyzer import Analyzer

st.set_page_config(page_title="Flight Dashboard")
#st.info("Use the sidebar to navigate between pages.")


st.sidebar.markdown("---")
st.sidebar.write("Filters coming soon...")


 
# STEP 3 (still here)
st.title("Airline Delay Dashboard")
st.write("Delay System!")


#connect to DB
conn = sqlite3.connect("Airline_delay.db")
df = pd.read_sql("SELECT * FROM delays", conn)

#st.subheader("Raw Data")
#st.dataframe(df.head())


# Add filters (this is where Streamlit shines)
years = sorted(df['year'].dropna().unique())
selected_year = st.selectbox("Select Year", years)
filtered_df = df[df['year'] == selected_year]



#st.sidebar.header("Filters")
#selected_year = st.sidebar.selectbox("Select Year", years)

# Airline performance chart
import matplotlib.pyplot as plt

airline_perf = (
    filtered_df.groupby('carrier_name')['arr_delay']
    .mean()
    .sort_values()
)

#fig, ax = plt.subplots(figsize=(12,6))
#airline_perf.plot(kind='barh', ax=ax)

#ax.set_title(f"Average Delay by Airline ({selected_year})")
#ax.set_xlabel("Delay (minutes)")

#st.pyplot(fig)




#state col
state_delay = (
    filtered_df.groupby('state')['arr_delay']
    .mean()
    .sort_values(ascending=False)
    .head(15)
)

#fig, ax = plt.subplots()
#state_delay.plot(kind='bar', ax=ax)
#ax.set_title("Top 15 States by Delay")
#st.pyplot(fig)


# causes of delays
delay_factors = filtered_df[[
    'carrier_delay',
    'weather_delay',
    'nas_delay',
    'security_delay',
    'late_aircraft_delay'
]].sum()

fig, ax = plt.subplots()
delay_factors.sort_values().plot(kind='barh', ax=ax)
ax.set_title("Delay Causes Contribution")
st.pyplot(fig)

####################################################################################################
####################################################################################################
# BOTTLE NECK ANALYSIS HERE
# from Analyzer class
analyzer = Analyzer(filtered_df)
bottlenecks = analyzer.airport_bottlenecks()

st.subheader("Airport Bottlenecks")
top_n = st.slider("Select number of airports", 5, 20, 10)
top_bottlenecks = bottlenecks.head(top_n)
st.dataframe(top_bottlenecks)

#plot above
fig, ax = plt.subplots(figsize=(12,6))

top_bottlenecks['avg_delay'].sort_values().plot(
    kind='barh',
    ax=ax
)

ax.set_title("Airports with Highest Average Delays")
ax.set_xlabel("Average Delay (minutes)")

st.pyplot(fig)

#traffice vs delay
fig, ax = plt.subplots(figsize=(10,6))

ax.scatter(
    bottlenecks['traffic'],
    bottlenecks['avg_delay']
)

ax.set_xlabel("Traffic (Number of Flights)")
ax.set_ylabel("Average Delay")
ax.set_title("Airport Bottlenecks: Traffic vs Delay")

st.pyplot(fig)


min_traffic = st.slider("Minimum Traffic", 0, int(bottlenecks['traffic'].max()), 100)
filtered = bottlenecks[bottlenecks['traffic'] >= min_traffic]



fig, ax = plt.subplots(figsize=(12,6))
filtered.sort_values(by='avg_delay').tail(10)['avg_delay'].plot(
    kind='barh',
    ax=ax
)

st.pyplot(fig)

# BOTTLE NECK ANALYSIS END
##
##################################################

##################################################
#airline_reliability

analyzer = Analyzer(filtered_df)
reliability = analyzer.airline_reliability()


st.subheader("Airline Reliability: Which airline is most reliable")
top_n = st.slider("Number of airlines", 5, 20, 10)
top_airlines = reliability.head(top_n)
st.dataframe(top_airlines)



fig, ax = plt.subplots(figsize=(12,6))
top_airlines['delay_rate'].sort_values().plot(
    kind='barh',
    ax=ax
)
ax.set_title("Airline Delay Rate (Lower is Better)")
ax.set_xlabel("Delay Rate")
st.pyplot(fig)



#fig, ax = plt.subplots(figsize=(12,6))
#top_airlines['avg_delay'].sort_values().plot(
#    kind='barh',
#    ax=ax
#)
#ax.set_title("Average Delay by Airline")
#ax.set_xlabel("Minutes")
#st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(
    reliability['delay_rate'],
    reliability['avg_delay']
)
for airline in reliability.index:
    ax.text(
        reliability.loc[airline, 'delay_rate'],
        reliability.loc[airline, 'avg_delay'],
        airline,
        fontsize=10
    )
ax.set_xlabel("Delay Rate")
ax.set_ylabel("Average Delay (minutes)")
ax.set_title("Airline Reliability: Delay Rate vs Avg Delay")

st.pyplot(fig)




#Quadrant	Meaning
#Low delay_rate + low delay     	✅ Best airlines
#High delay_rate + high delay	    ❌ Worst airlines
#Low rate + high delay	            ⚠️ rare but severe delays
#High rate + low delay	            ⚠️ frequent small delays





fig, ax = plt.subplots(figsize=(10,6))

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
ax.text(x_mean * 1.5, y_mean * 1.2, "Worst", fontsize=12, color='red')
ax.text(x_mean * 0.4, y_mean * 0.8, "Best", fontsize=12, color='green')
ax.text(x_mean * 1.5, y_mean * 0.8, "Frequent Small Delays", fontsize=12, color='green')

st.pyplot(fig)
##################################################
###################### Airline Delay Rate  ############################


analyzer = Analyzer(filtered_df)
monthly_delays = analyzer.month_with_highest_delay()
#print(monthly_delays)

# monthly_delays['delay_rate_2'].plot(kind='bar')

# plt.title("Delay Rate by Month")
# plt.xlabel("Month")
# plt.ylabel("Delay Rate")
# plt.xticks(rotation=0)
# plt.show()


fig, ax = plt.subplots(figsize=(12,8))
monthly_delays.sort_values(by='month').plot(
    kind='bar',
    ax=ax
)
ax.set_title("Airline Delay Rate")
ax.set_xlabel("Delay Rate")
st.pyplot(fig)


####################################################################################################
####################################################################################################
# factors most influence delay

