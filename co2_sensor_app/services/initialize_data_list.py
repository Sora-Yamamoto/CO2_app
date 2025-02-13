import streamlit as st


def initialize_pw_data():
    # Data initialization in session_state
    st.session_state.pw_year = []
    st.session_state.pw_month = []
    st.session_state.pw_day = []
    st.session_state.pw_hour = []
    st.session_state.pw_minute = []
    st.session_state.pw_second = []
    st.session_state.pw_state = []
    st.session_state.pw_sig_dark = []
    st.session_state.pw_sig_435nm = []
    st.session_state.pw_sig_490nm = []
    st.session_state.pw_sig_590nm = []
    st.session_state.pw_sig_735nm = []
    st.session_state.pw_ref_dark = []
    st.session_state.pw_ref_435nm = []
    st.session_state.pw_ref_490nm = []
    st.session_state.pw_ref_590nm = []
    st.session_state.pw_ref_735nm = []
    st.session_state.pw_measurement_number = []
    st.session_state.pw_time = []
    st.session_state.pw_I_435nm = []
    st.session_state.pw_I_490nm = []
    st.session_state.pw_I_590nm = []
    st.session_state.pw_I_735nm = []


def initialize_co2_data():
    (
        st.session_state.co2_year,
        st.session_state.co2_month,
        st.session_state.co2_day,
        st.session_state.co2_hour,
        st.session_state.co2_minute,
        st.session_state.co2_second,
        st.session_state.co2_state,
    ) = ([] for _ in range(7))
    (
        st.session_state.co2_sig_dark,
        st.session_state.co2_sig_435nm,
        st.session_state.co2_sig_490nm,
        st.session_state.co2_sig_590nm,
        st.session_state.co2_sig_735nm,
    ) = ([] for _ in range(5))
    (
        st.session_state.co2_ref_dark,
        st.session_state.co2_ref_435nm,
        st.session_state.co2_ref_490nm,
        st.session_state.co2_ref_590nm,
        st.session_state.co2_ref_735nm,
    ) = ([] for _ in range(5))
    st.session_state.co2_measurement_number = []
    st.session_state.co2_time = []
    (
        st.session_state.co2_I_435nm,
        st.session_state.co2_I_490nm,
        st.session_state.co2_I_590nm,
        st.session_state.co2_I_735nm,
    ) = ([] for _ in range(4))
    (
        st.session_state.co2_A_435nm,
        st.session_state.co2_A_490nm,
        st.session_state.co2_A_590nm,
        st.session_state.co2_A_735nm,
        st.session_state.co2_A_R,
    ) = ([] for _ in range(5))
