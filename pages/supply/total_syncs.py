import streamlit as st
from utils.navigation import set_query_params

def show():
    st.title("Total Full Syncs")
    st.write("Details of total full syncs will be displayed here.")
    if st.button("Back to Supply"):
        set_query_params(page='supply')
