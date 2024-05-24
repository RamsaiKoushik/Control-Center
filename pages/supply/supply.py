import streamlit as st
import datetime
from utils.navigation import set_query_params
from utils.sync_data import get_full_sync_data

def show():
    st.title("Supply Page")

    # Displaying today's date by default with an option to change
    selected_date = st.date_input("Select Date", st.session_state.get('selected_date', datetime.date.today()))
    st.session_state.selected_date = selected_date

    # Fetch full sync details (replace with actual data fetching logic)
    full_sync_data = get_full_sync_data(selected_date)

    st.write(f"Full Sync Details for {selected_date}")
    if st.button(f"Successful Full Syncs: {full_sync_data['successful']}"):
        set_query_params(page='successful_syncs')
    if st.button(f"Failed Full Syncs: {full_sync_data['failed']}"):
        set_query_params(page='failed_syncs')
    if st.button(f"Total Full Syncs: {full_sync_data['total']}"):
        set_query_params(page='total_syncs')
