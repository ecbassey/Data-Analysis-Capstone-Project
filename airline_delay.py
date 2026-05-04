import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

#from data_loader import DataLoader
#from data_cleaner import DataCleaner
from analyzer import Analyzer

def show():
    st.title("Airline Analysis Page")

#st.title("Airline Analysis Page")
#st.write("This is where analysis happens")