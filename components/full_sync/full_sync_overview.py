# components/full_sync/full_sync_overview.py
import streamlit as st
from data.data_fetcher import fetch_data

def display_full_sync_overview():
    query = """
    SELECT status, COUNT(*) as count
    FROM full_sync
    GROUP BY status;
    """
    data = fetch_data(query)
    st.write("### Full Sync Overview")
    st.bar_chart(data.set_index('status')['count'])
