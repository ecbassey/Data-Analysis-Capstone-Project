import streamlit as st
import matplotlib.pyplot as plt
from data_loader import DataLoader
from data_cleaner import DataCleaner
from analyzer import Analyzer

st.markdown("""
    <style>
    .stApp {
        background-color: #b3e0dc;
        color: white;
    }

    h1, h2, h3 {
        color: ##00C4B4;
    }
    </style>
""", unsafe_allow_html=True)


st.set_page_config(layout="wide")
#st.title("Airline Delay Intelligence System")
st.markdown("""
    <h1 style='
        text-align: center; 
        color: #088f8f;
        font-weight: 700;
    '>
        U.S. Airline Delay Intelligence System
    </h1>
    <h3 style='
        text-align: center; 
        color: #088f8f;
        font-weight: 300;
    '>
            Understanding the Causes and Patterns of Airline Delays and Cancellations
    </h3>
""", unsafe_allow_html=True)

st.write("\n") #Line break
st.write("\n") #Line break
# tab1, tab2, tab3 = st.tabs(["Overview", "Analysis", "Predictions"])

# with tab1:
#     st.write("Overview content")

# with tab2:
#     st.write("Analysis content")


#st.subheader("Airline Delay Dashboard")
#st.write("Welcome to your airline analytics app")



col1, col2 = st.columns(2)

with col1:
    st.header("Analysis Objectives")
    st.text("This project aims to identify the most reliable airlines, peak delay periods, major airport bottlenecks,"
    " and key factors driving delays, while uncovering geographic patterns to support data-driven insights "
    "and operational improvements.")
   
with col2:
    st.image("pages/delay1.jpg")
    # st.subheader("Column 2")
    # st.write("More content here")





def card(title, value):
    st.markdown(f"""
        <div style="
            background-color:#1c1f26;
            padding:20px;
            border-radius:15px;
            box-shadow: 10px 4px 10px rgba(0,0,0,0.3);
        ">
            <h2 style="color: #088f8f;">{title}</h2>
            <h4>{value}</h4>
        </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    card("20% to 30%", "U.S. flights are delayed each year")

with col2:
    card("1.5% to 2.5%", "U.S. flights are cancelled each year")

st.write("\n") #Line break


def card(title, value):
    st.markdown(f"""
        <div style="
            background-color:#1c1f26;
            padding:20px;
            bottom-padding:20px;
            border-radius:15px;
            box-shadow: 10px 4px 10px rgba(0,0,0,0.3);
        ">
            <h2 style="color: #088f8f;">{title}</h2>
            <h4>{value}</h4>
        </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    card("18% to 28%", "Global flights are delayed each year")

with col2:
    card("25% to 40%", "African flights are delayed or cancelled")
    
st.write("\n") #Line break

#OBJECTIVES

def card(title, value):
    st.markdown(f"""
        <div style="
            background-color:#088f8f;
            padding:20px;
            padding-left:40px;
            border-radius:15px;
            box-shadow: 10px 4px 10px rgba(0,0,0,0.3);
        ">
            <h2 style="color: #000000;">{title}</h2>
            <h4 style="font-size:18px;">{value}</h4>            
        </div>
    """, unsafe_allow_html=True)

card("Project aims to:", """
- Analyze Which airline is most reliable. <br>
- Identify any time-based trends in delays (which month/seasons has more delays).<br>
- Evaluate industry recover after COVID. <br>
- Identify which airports are bottlenecks.<br> 
- Identify what factors most influence delays.<br>
- Analyze delay and cancellation patterns across different airlines.
""")

st.write("\n")
card("Data Source:", """
- Bureau of Transportation Statistics. <br>
- U.S. Department of Transportation
""")
st.write("\n")
card("Project Preparation:", """
- Data ingestion: CSV <br>
- Data Transformation: BigQuery <br>
- Data Storage: SQL <br>
- Data cleaning & analysis: Python / Pandas <br>
- Software design: OOP <br>
- Visualization: matplotlib / seaborn / GeoPandas
""")


# col1, col2 = st.columns(2)

# with col1:
   
#     st.markdown("""
#     - Delay Analysis
#     - Weather Impact
#     - Carrier Issues
#     """)

# with col2:
#     st.markdown("""
#     - Security Delays
#     - NAS Delays
#     - Late Aircraft
#     """)

