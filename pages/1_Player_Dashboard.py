import streamlit as st
import pandas as pd

st.title("Player Dashboard")

st.write("Upload or load your player data here.")

uploaded = st.file_uploader("Upload players.csv", type="csv")

if uploaded:
    players = pd.read_csv(uploaded)
    st.dataframe(players)
