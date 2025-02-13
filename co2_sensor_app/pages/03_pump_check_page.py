import streamlit as st
from services import serial_service

st.title("Pump Check Page")

# Flow rate selection (1-60)
pump1_flow_rate = st.slider("Pump 1 Flow Rate", min_value=1, max_value=60, value=60)
pump2_flow_rate = st.slider("Pump 2 Flow Rate", min_value=1, max_value=60, value=60)

# Pump control buttons
if st.button("Pump 1 ON"):
    TxData = f"TP11{pump1_flow_rate}\r"  # Dynamic flow rate selection
    if st.session_state.ser:  # シリアルポートが開いている場合のみ送信
        st.session_state.ser.write(TxData.encode("utf-8"))

if st.button("Pump 1 OFF"):
    TxData = "TP10\r"  # Stop pump 1
    if st.session_state.ser:  # シリアルポートが開いている場合のみ送信
        st.session_state.ser.write(TxData.encode("utf-8"))

if st.button("Pump 2 ON"):
    TxData = f"TP21{pump2_flow_rate}\r"  # Dynamic flow rate selection
    if st.session_state.ser:  # シリアルポートが開いている場合のみ送信
        st.session_state.ser.write(TxData.encode("utf-8"))

if st.button("Pump 2 OFF"):
    TxData = "TP20\r"  # Stop pump 2
    if st.session_state.ser:  # シリアルポートが開いている場合のみ送信
        st.session_state.ser.write(TxData.encode("utf-8"))

# Flash memory delete function
if st.button("Delete Flash Memory"):
    serial_service.delete_FlashMemory()
