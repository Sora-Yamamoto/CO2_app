import streamlit as st
from services import make_date_folder, save_data_to_csv, save_data_to_image, serial_service
from services.co2_measurement import start_measurement_co2

st.title("CO2 Measurement")

# 初期化処理
if "I_435nm_ave" not in st.session_state:
    st.session_state.I_435nm_ave = 1.9497885376366615  # 初期値を適切に設定
if "I_490nm_ave" not in st.session_state:
    st.session_state.I_490nm_ave = 2.2112016069155542
if "I_590nm_ave" not in st.session_state:
    st.session_state.I_590nm_ave = 0.8408672705516362
if "I_735nm_ave" not in st.session_state:
    st.session_state.I_735nm_ave = 0.8317714985217586


# センサーの光学測定データを表示
st.write("I_435nm_ave: ", st.session_state.I_435nm_ave)
st.write("I_490nm_ave: ", st.session_state.I_490nm_ave)
st.write("I_590nm_ave: ", st.session_state.I_590nm_ave)
st.write("I_735nm_ave: ", st.session_state.I_735nm_ave)

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

# ボタンレイアウト（2カラム）
col1, col2 = st.columns(2)

with col1:
    if st.button("Stop Measurement"):
        serial_service.stop_pump1()
        st.success("Measurement Stopped")

with col2:
    if st.button("Stop Measurement & Save Data"):
        serial_service.stop_pump1()
        make_date_folder.make_date_folder()
        output_df = save_data_to_csv.save_co2_csv(ppm)
        save_data_to_image.save_co2_image(output_df, ppm)
        st.success("Measurement Stopped & Data Saved")

# ON/OFFボタンとしてのチェックボックス
is_on = st.checkbox("StableCheck ON/OFF", value=True)
stableCheck = is_on

# 測定開始ボタン
if st.button("Start Measurement"):
    st.success("Measurement Running")
    start_measurement_co2(M_time, ppm, stableCheck, st.session_state.measure_temp)  # 測定時の温度を session_state から取得
    st.success("Measurement Completed")
