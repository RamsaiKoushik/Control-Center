import streamlit as st

def set_query_params(page='home'):
    st.query_params['page'] = page
    # st.query_params.update(params)

def get_query_params():
    try: 
        print('just checking')
        return st.query_params['page']
    except:
        return 'home'