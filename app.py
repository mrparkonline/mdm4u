# MDM4U Course Website
# App built on Streamlit version 1.48.0
# gspread version: 6.2.1

# imports
import streamlit as st
st.set_page_config(layout="wide")

home = st.Page("pages/home.py", title="Data Management (MDM4U)")
u1_page = st.Page("pages/unit1.py", title="Unit 1 - Data and Statiscal Analysis", icon=":material/analytics:")
u2_page = st.Page("pages/unit2.py", title="Unit 2 - Probablity", icon=":material/casino:")

current_pg = home
pages = [home, u1_page, u2_page]
current_pg = st.navigation(pages, position="sidebar", expanded=True)
current_pg.run()
