import streamlit as st
import pandas as pd

st.title("Game Log Explorer")

uploaded = st.file_uploader("Upload events.csv", type="csv")

if uploaded:
    events = pd.read_csv(uploaded)
    st.dataframe(events)
