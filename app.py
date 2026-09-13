import streamlit as st

st.set_page_config(
    page_title="Sports Research Tool",
    page_icon="📊",
    layout="wide"
)

st.title("Sports Research Tool")
st.subheader("Home Screen Hub")

st.write("""
Welcome to your custom sports analytics system.
Use the navigation sidebar to access dashboards, tools, and EV engines.
""")

st.divider()

st.header("Quick Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/1_Player_Dashboard.py", label="Player Dashboard", icon="👤")

with col2:
    st.page_link("pages/2_Game_Log_Explorer.py", label="Game Log Explorer", icon="📈")

with col3:
    st.page_link("pages/3_Props_EV_Engine.py", label="Props & EV Engine", icon="🎯")

col4, col5, col6 = st.columns(3)

with col4:
    st.page_link("pages/4_Data_Model_Viewer.py", label="Data Model Viewer", icon="🗂️")

with col5:
    st.page_link("pages/5_API_Tools.py", label="API Tools", icon="🔌")

with col6:
    st.page_link("pages/6_Hosted_App.py", label="Hosted App", icon="🌐")
