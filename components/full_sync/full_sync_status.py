# components/full_sync/full_sync_status.py
import streamlit as st
from data.data_fetcher import fetch_data

def display_full_sync_status():
    query = """
    SELECT node, status, COUNT(*) as count
    FROM full_sync
    GROUP BY node, status;
    """
    data = fetch_data(query)
    st.write("### Full Sync Status by Node")
    st.dataframe(data)
