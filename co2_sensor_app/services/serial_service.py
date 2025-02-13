import serial
import streamlit as st


def open_serial_port():
    try:
        st.session_state.ser = serial.Serial("COM7", 19200, timeout=1)  # 有線の場合はCOM5,無線の場合はCOM8
        if st.session_state.ser.is_open:
            st.success("Serial communication established successfully.")
        else:
            st.error("Failed to establish serial communication.")
            st.session_state.ser.close()
            st.stop()
    except serial.SerialException as e:
        st.error(f"Error opening serial port: {e}")


def close_serial_port():
    if st.session_state.ser and st.session_state.ser.is_open:
        st.session_state.ser.close()
        st.success("Serial port closed.")
    else:
        st.warning("Serial port already closed or not initialized.")


def stop_measurement():
    if st.session_state.ser and st.session_state.ser.is_open:
        stop_text = "SE\r"
        st.session_state.ser.write(stop_text.encode())
    else:
        st.warning("Serial port not open. Cannot stop measurement.")


def drive_pump1():
    if st.session_state.ser and st.session_state.ser.is_open:
        stop_text = "TP1160\r"  # 送信するデータ,TP11&Freq,Freqは1~60なら動く？？
        st.session_state.ser.write(stop_text.encode())
    else:
        st.warning("Serial port not open.")


def stop_pump1():
    if st.session_state.ser and st.session_state.ser.is_open:
        stop_text = "TP10\r"
        st.session_state.ser.write(stop_text.encode())
    else:
        st.warning("Serial port not open.")


def drive_pump2():
    if st.session_state.ser and st.session_state.ser.is_open:
        stop_text = "TP2160\r"  # 送信するデータ,TP21&Freq,Freqは1~60なら動く？？
        st.session_state.ser.write(stop_text.encode())
    else:
        st.warning("Serial port not open.")


def stop_pump2():
    if st.session_state.ser and st.session_state.ser.is_open:
        stop_text = "TP20\r"
        st.session_state.ser.write(stop_text.encode())
    else:
        st.warning("Serial port not open.")


def delete_FlashMemory():
    if st.session_state.ser and st.session_state.ser.is_open:
        text = "TFC\r"
        st.session_state.ser.write(text.encode())
        st.success("Flash Memory Deleted.")
    else:
        st.warning("Serial port not open.")
