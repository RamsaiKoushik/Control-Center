# components/delta_sync/delta_sync_events.py
import streamlit as st
from data.data_fetcher import fetch_data

def display_delta_sync_events():
    query = """
    SELECT event_type, COUNT(*) as count
    FROM delta_sync
    GROUP BY event_type;
    """
    data = fetch_data(query)
    st.write("### Delta Sync Events")
    st.bar_chart(data.set_index('event_type')['count'])
