import streamlit as st
from services import serial_service


def main():
    st.set_page_config(page_title="My Custom App", layout="wide")

    # Initialize Streamlit session state
    if "ser" not in st.session_state:
        st.session_state.ser = None

    # Initialize the measurement averages in session state if not already present
    # if "I_435nm_ave" not in st.session_state:
    #     st.session_state.I_435nm_ave = 1.944
    # if "I_490nm_ave" not in st.session_state:
    #     st.session_state.I_490nm_ave = 2.143
    # if "I_590nm_ave" not in st.session_state:
    #     st.session_state.I_590nm_ave = 0.846
    # if "I_735nm_ave" not in st.session_state:
    #     st.session_state.I_735nm_ave = 0.848
    # if "I_435nm_ave" not in st.session_state:
    #     st.session_state.I_435nm_ave = 1.546
    # if "I_490nm_ave" not in st.session_state:
    #     st.session_state.I_490nm_ave = 1.591
    # if "I_590nm_ave" not in st.session_state:
    #     st.session_state.I_590nm_ave = 0.662
    # if "I_735nm_ave" not in st.session_state:
    #     st.session_state.I_735nm_ave = 0.669
    if "I_435nm_ave" not in st.session_state:
        st.session_state.I_435nm_ave = 1.9497885376366615
    if "I_490nm_ave" not in st.session_state:
        st.session_state.I_490nm_ave = 2.2112016069155542
    if "I_590nm_ave" not in st.session_state:
        st.session_state.I_590nm_ave = 0.8408672705516362
    if "I_735nm_ave" not in st.session_state:
        st.session_state.I_735nm_ave = 0.8317714985217586

    # Open the serial port initially
    if st.session_state.ser is None or not st.session_state.ser.is_open:
        serial_service.open_serial_port()

    # タイトル
    st.title("co2 sensor Application")
    # # ヘッダ
    # st.header("Header")
    # # サブレベルヘッダ
    # st.subheader("Sub header")
    # 純粋なテキスト
    st.text("左のサイドバーから操作を選択してください。")


if __name__ == "__main__":
    main()

# streamlit run co2_sensor_app/home.py
