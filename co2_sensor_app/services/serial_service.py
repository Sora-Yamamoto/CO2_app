import serial
import streamlit as st


def open_serial_port():
    """ シリアルポートを開く """
    try:
        st.session_state.ser = serial.Serial("COM7", 19200, timeout=1)  # 有線の場合はCOM5, 無線の場合はCOM8
        if st.session_state.ser.is_open:
            st.success("✅ Serial communication established successfully.")
        else:
            st.error("❌ Failed to establish serial communication.")
            st.session_state.ser.close()
            st.stop()
    except serial.SerialException:
        st.warning("⚠️ Serial port not open. Running in simulation mode.")
        st.session_state.ser = None  # シミュレーションモードに切り替え


def close_serial_port():
    """ シリアルポートを閉じる """
    if "ser" in st.session_state and st.session_state.ser and st.session_state.ser.is_open:
        st.session_state.ser.close()
        st.success("✅ Serial port closed.")
    else:
        st.warning("⚠️ Serial port already closed or not initialized.")


def send_command(command, description):
    """ シリアルポートが開いている場合にコマンドを送信 """
    if "ser" in st.session_state and st.session_state.ser:
        st.session_state.ser.write(command.encode())
        st.success(f"✅ {description}: {command.strip()}")
    else:
        st.warning(f"⚠️ Serial port not open, but simulating {description}: {command.strip()}")


def stop_measurement():
    send_command("SE\r", "Stopping measurement")


def drive_pump1():
    send_command("TP1160\r", "Driving Pump 1")


def stop_pump1():
    send_command("TP10\r", "Stopping Pump 1")


def drive_pump2():
    send_command("TP2160\r", "Driving Pump 2")


def stop_pump2():
    send_command("TP20\r", "Stopping Pump 2")


def delete_FlashMemory():
    send_command("TFC\r", "Deleting Flash Memory")


#import serial
#import streamlit as st


#def open_serial_port():
    #try:
        #st.session_state.ser = serial.Serial("COM7", 19200, timeout=1)  # 有線の場合はCOM5,無線の場合はCOM8
        #if st.session_state.ser.is_open:
            #st.success("Serial communication established successfully.")
        #else:
            #st.error("Failed to establish serial communication.")
            #st.session_state.ser.close()
            #st.stop()
    #except serial.SerialException as e:
        #st.error(f"Error opening serial port: {e}")


#def close_serial_port():
    #if st.session_state.ser and st.session_state.ser.is_open:
        #st.session_state.ser.close()
        #st.success("Serial port closed.")
    #else:
        #st.warning("Serial port already closed or not initialized.")


#def stop_measurement():
    #if st.session_state.ser and st.session_state.ser.is_open:
        #stop_text = "SE\r"
        #st.session_state.ser.write(stop_text.encode())
    #else:
        #st.warning("Serial port not open. Cannot stop measurement.")


#def drive_pump1():
    #if st.session_state.ser and st.session_state.ser.is_open:
        #stop_text = "TP1160\r"  # 送信するデータ,TP11&Freq,Freqは1~60なら動く？？
        #st.session_state.ser.write(stop_text.encode())
    #else:
        #st.warning("Serial port not open.")


#def stop_pump1():
    #if st.session_state.ser and st.session_state.ser.is_open:
        #stop_text = "TP10\r"
        #st.session_state.ser.write(stop_text.encode())
    #else:
        #st.warning("Serial port not open.")


#def drive_pump2():
    #if st.session_state.ser and st.session_state.ser.is_open:
        #stop_text = "TP2160\r"  # 送信するデータ,TP21&Freq,Freqは1~60なら動く？？
        #st.session_state.ser.write(stop_text.encode())
    #else:
        #st.warning("Serial port not open.")


#def stop_pump2():
    #if st.session_state.ser and st.session_state.ser.is_open:
        #stop_text = "TP20\r"
        #st.session_state.ser.write(stop_text.encode())
    #else:
        #st.warning("Serial port not open.")


#def delete_FlashMemory():
    #if st.session_state.ser and st.session_state.ser.is_open:
        #text = "TFC\r"
        #st.session_state.ser.write(text.encode())
        #st.success("Flash Memory Deleted.")
    #else:
        #st.warning("Serial port not open.")
