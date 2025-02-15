import streamlit as st

# タイトル
st.title("Pump Check Page")

# シリアルポートなしでも動作するための初期化
if "pump1_status" not in st.session_state:
    st.session_state["pump1_status"] = "OFF"
if "pump2_status" not in st.session_state:
    st.session_state["pump2_status"] = "OFF"

# Flow rate selection (1-60)
pump1_flow_rate = st.slider("Pump 1 Flow Rate", min_value=1, max_value=60, value=60)
pump2_flow_rate = st.slider("Pump 2 Flow Rate", min_value=1, max_value=60, value=60)

# Pump control buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Pump 1 ON"):
        if "ser" in st.session_state and st.session_state.ser:
            TxData = f"TP11{pump1_flow_rate}\r"
            st.session_state.ser.write(TxData.encode("utf-8"))
            st.session_state["pump1_status"] = "ON"
            st.success(f"Pump 1 started at {pump1_flow_rate} flow rate")
        else:
            st.session_state["pump1_status"] = "ON"
            st.warning("⚠️ Serial port not open, but simulating Pump 1 ON")

    if st.button("Pump 1 OFF"):
        if "ser" in st.session_state and st.session_state.ser:
            TxData = "TP10\r"
            st.session_state.ser.write(TxData.encode("utf-8"))
            st.session_state["pump1_status"] = "OFF"
            st.success("Pump 1 stopped")
        else:
            st.session_state["pump1_status"] = "OFF"
            st.warning("⚠️ Serial port not open, but simulating Pump 1 OFF")

with col2:
    if st.button("Pump 2 ON"):
        if "ser" in st.session_state and st.session_state.ser:
            TxData = f"TP21{pump2_flow_rate}\r"
            st.session_state.ser.write(TxData.encode("utf-8"))
            st.session_state["pump2_status"] = "ON"
            st.success(f"Pump 2 started at {pump2_flow_rate} flow rate")
        else:
            st.session_state["pump2_status"] = "ON"
            st.warning("⚠️ Serial port not open, but simulating Pump 2 ON")

    if st.button("Pump 2 OFF"):
        if "ser" in st.session_state and st.session_state.ser:
            TxData = "TP20\r"
            st.session_state.ser.write(TxData.encode("utf-8"))
            st.session_state["pump2_status"] = "OFF"
            st.success("Pump 2 stopped")
        else:
            st.session_state["pump2_status"] = "OFF"
            st.warning("⚠️ Serial port not open, but simulating Pump 2 OFF")

# 現在のポンプ状態表示
st.write(f"🔵 **Pump 1 Status:** {st.session_state['pump1_status']}")
st.write(f"🟢 **Pump 2 Status:** {st.session_state['pump2_status']}")

# Flash memory delete function
if st.button("Delete Flash Memory"):
    if "ser" in st.session_state and st.session_state.ser:
        st.session_state.ser.write("DELETE_FLASH\r".encode("utf-8"))
        st.success("Flash Memory Deleted")
    else:
        st.warning("⚠️ Serial port not open, but simulating Flash Memory Delete")
