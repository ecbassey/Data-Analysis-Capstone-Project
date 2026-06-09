import streamlit as st
import matplotlib.pyplot as plt
from data_loader import DataLoader
from data_cleaner import DataCleaner
from analyzer import Analyzer

st.set_page_config(layout="wide")


tab1, tab2, tab3 = st.tabs(["Overview", "Analysis", "Predictions"])

with tab1:
    st.write("Overview content")

with tab2:
    st.write("Analysis content")


# st.markdown("""
#     <style>
#     .stApp {
#         background-image: url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee");
#         background-size: cover;
#     }
#     </style>
# """, unsafe_allow_html=True)

st.markdown("""
    <style>
    .stApp {
        background-color: #b3e0dc;
        color: white;
    }

    .block-container {
        padding-top: 2rem;
    }

    h1, h2, h3 {
        color: ##00C4B4;
    }
    </style>
""", unsafe_allow_html=True)



st.title("✈️ Airline Delay Dashboard")
st.write("Welcome to your airline analytics app")




col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.metric("Total Flights", "120,000")

with col2:
    st.metric("Avg Delay", "12 min")

with col3:
    st.metric("Delay Rate", "32%", help="Percentage of delayed flights")





def card(title, value):
    st.markdown(f"""
        <div style="
            background-color:#1c1f26;
            padding:20px;
            border-radius:15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        ">
            <h4>{title}</h4>
            <h2>{value}</h2>
        </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    card("Total Flights", "120,000")

with col2:
    card("Delayed Flights", "38,000")




