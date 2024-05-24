# components/poison_pill/poison_pill_monitor.py
import streamlit as st
from data.data_fetcher import fetch_data

def display_poison_pill_monitor():
    query = """
    SELECT queue_type, message_type, COUNT(*) as count
    FROM poison_pill_dlq
    GROUP BY queue_type, message_type;
    """
    data = fetch_data(query)
    st.write("### Poison Pill & DLQ Monitor")
    st.dataframe(data)