import streamlit as st
from pages import home
from pages.supply import supply, successful_syncs, failed_syncs, total_syncs
from utils.navigation import get_query_params, set_query_params

# # Initialize session state
# if 'page' not in st.session_state:
#     st.session_state.page = 'home'

# Get the page from query params
# params = get_query_params()
# page = params.get('page', ['home'])[0]

# page = st.session_state.page

page = get_query_params()

# Routing Logic
if page == 'home':
    home.show()
elif page == 'supply':
    supply.show()
elif page == 'successful_syncs':
    successful_syncs.show()
elif page == 'failed_syncs':
    failed_syncs.show()
elif page == 'total_syncs':
    total_syncs.show()
else:
    st.write("Page not found!")

# Set the page in session state to persist navigation
# st.session_state.page = page

# set_query_params(page=page)
st.session_state.page = page