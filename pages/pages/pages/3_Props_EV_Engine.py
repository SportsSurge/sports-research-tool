import streamlit as st
import pandas as pd

st.title("Props & EV Engine")

uploaded = st.file_uploader("Upload props.csv", type="csv")

if uploaded:
    props = pd.read_csv(uploaded)
    st.dataframe(props)
