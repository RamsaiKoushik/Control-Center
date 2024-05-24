# app.py
import streamlit as st
from components.full_sync.full_sync_overview import display_full_sync_overview
from components.full_sync.full_sync_status import display_full_sync_status
from components.delta_sync.delta_sync_events import display_delta_sync_events
# from components.poison_pill.poison_pill_monitor import display_poison_pill_monitor

st.title("Operational Visibility Dashboard")

# Display each section
st.header("Full Sync")
display_full_sync_overview()
display_full_sync_status()

st.header("Delta Sync")
display_delta_sync_events()

st.header("Poison Pill & DLQ Monitor")
# display_poison_pill_monitor()
