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

st.set_page_config(layout="centered")
st.title("Insights & Recommendation")



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

card("Insights:", """
- Airline Reliability Varies Significantly: Operational efficiency differs across carriers. <br><br>
- Delays Increase during the summer months: Corresponds to an increase in total flights.<br><br>
- Major Bottlenecks: Airports with highest traffic also show higher delay times.  <br><br>
- Hub-heavy regions have more congestion<br><br> <br>
- Cancelations are higher during summer months<br><br>
""")