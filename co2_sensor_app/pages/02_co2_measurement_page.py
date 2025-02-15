import streamlit as st
from services import make_date_folder, save_data_to_csv, save_data_to_image, serial_service
from services.co2_measurement import start_measurement_co2

st.title("CO2 Measurement")

# シリアルポートなしでも動作するための初期化
if "measurement_status" not in st.session_state:
    st.session_state["measurement_status"] = "STOPPED"

# 初期化処理（光学測定データのセッションステートを設定）
sensor_defaults = {
    "I_435nm_ave": 1.9497885376366615,
    "I_490nm_ave": 2.2112016069155542,
    "I_590nm_ave": 0.8408672705516362,
    "I_735nm_ave": 0.8317714985217586,
}

for key, value in sensor_defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# センサーの光学測定データを表示
st.write(f"🔵 **I_435nm_ave:** {st.session_state.I_435nm_ave}")
st.write(f"🟢 **I_490nm_ave:** {st.session_state.I_490nm_ave}")
st.write(f"🟡 **I_590nm_ave:** {st.session_state.I_590nm_ave}")
st.write(f"🔴 **I_735nm_ave:** {st.session_state.I_735nm_ave}")

# 測定時間の設定（スライダー）
default_time = 1500
M_time = st.slider("Quick Set Measurement Time (seconds)", min_value=100, max_value=9999, value=default_time, step=10)

# CO2 濃度の選択
ppm = st.selectbox("CO2 concentration", options=["482ppm", "842ppm", "1350ppm", "field"])

# 測定時の温度の入力（0.5℃単位）
if "measure_temp" not in st.session_state:
    st.session_state.measure_temp = 25.0  # 初期値 25℃

st.session_state.measure_temp = st.number_input(
    "Measurement Temperature (°C)", min_value=0.0, max_value=50.0, value=st.session_state.measure_temp, step=0.5
)

# ON/OFFボタンとしてのチェックボックス
stableCheck = st.checkbox("StableCheck ON/OFF", value=True)

# ボタンレイアウト（2カラム）
col1, col2 = st.columns(2)

with col1:
    if st.button("Stop Measurement"):
        if "ser" in st.session_state and st.session_state.ser:
            serial_service.stop_pump1()
            st.session_state["measurement_status"] = "STOPPED"
            st.success("Measurement Stopped")
        else:
            st.session_state["measurement_status"] = "STOPPED"
            st.warning("⚠️ Serial port not open, but simulating Stop Measurement")

with col2:
    if st.button("Stop Measurement & Save Data"):
        if "ser" in st.session_state and st.session_state.ser:
            serial_service.stop_pump1()
            make_date_folder.make_date_folder()
            output_df = save_data_to_csv.save_co2_csv(ppm)
            save_data_to_image.save_co2_image(output_df, ppm)
            st.success("Measurement Stopped & Data Saved")
        else:
            st.warning("⚠️ Serial port not open, but simulating Data Save")
            st.session_state["measurement_status"] = "STOPPED"

# 測定開始ボタン
if st.button("Start Measurement"):
    if "ser" in st.session_state and st.session_state.ser:
        start_measurement_co2(M_time, ppm, stableCheck, st.session_state.measure_temp)
        st.session_state["measurement_status"] = "RUNNING"
        st.success("Measurement Running")
    else:
        st.warning("⚠️ Serial port not open, but simulating Start Measurement")
        st.session_state["measurement_status"] = "RUNNING"

# 現在の測定状態を表示
if st.session_state["measurement_status"] == "RUNNING":
    st.info("🚀 **Measurement is currently RUNNING**")
elif st.session_state["measurement_status"] == "STOPPED":
    st.info("⛔ **Measurement is STOPPED**")
