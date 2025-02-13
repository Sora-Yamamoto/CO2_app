import streamlit as st


def calculate_display_pw_I_ave():
    # Calculate the average of the last five values for each intensity list
    st.session_state.I_435nm_ave = sum(st.session_state.pw_I_435nm[-5:]) / 5
    st.session_state.I_490nm_ave = sum(st.session_state.pw_I_490nm[-5:]) / 5
    st.session_state.I_590nm_ave = sum(st.session_state.pw_I_590nm[-5:]) / 5
    st.session_state.I_735nm_ave = sum(st.session_state.pw_I_735nm[-5:]) / 5
    st.write("I_435nm_ave: ", st.session_state.I_435nm_ave)
    st.write("I_490nm_ave: ", st.session_state.I_490nm_ave)
    st.write("I_590nm_ave: ", st.session_state.I_590nm_ave)
    st.write("I_735nm_ave: ", st.session_state.I_735nm_ave)
