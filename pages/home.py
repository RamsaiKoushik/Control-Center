import streamlit as st
from utils.navigation import set_query_params

def show():
    st.title("Operational Center")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("SUPPLY"):
            print('just')
            set_query_params(page='supply')
    with col2:
        if st.button("DEMAND"):
            set_query_params(page='demand')  # Placeholder for demand page
    with col3:
        if st.button("Serviceability"):
            set_query_params(page='serviceability')  # Placeholder for serviceability page
