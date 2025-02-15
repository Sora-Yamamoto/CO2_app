import streamlit as st
import gspread
import pandas as pd
import json
import time
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API の認証
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_json = json.loads(st.secrets["GOOGLE_CREDENTIALS"])
CREDS = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, SCOPE)
CLIENT = gspread.authorize(CREDS)

# Google Sheets の設定
SPREADSHEET_ID = "1-yaWx4l0AS44lAv9SUBqAQaxSyQqYCGQqEBsl1Zn_Zs"  # Google Sheets の ID
SHEET = CLIENT.open_by_key(SPREADSHEET_ID).worksheet("PureWaterMeasurement")  # 「PureWaterMeasurement」シートを使用

# Streamlit タイトル
st.title("Pure Water Measurement")

# 測定時間の設定
default_time = 300
M_time = st.slider("Measurement Time (seconds)", min_value=10, max_value=1000, value=default_time, step=10)

# カスタム CSS
st.markdown(
    """
    <style>
        .big-font { font-size: 24px !important; }
        .red-text { color: red; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f'<p class="big-font">Selected Time: <span class="red-text">{M_time}</span> seconds</p>',
    unsafe_allow_html=True
)

# 測定データを Google Sheets に保存
def save_data_to_google_sheets(action, measurement_time=None, measurement_value=None):
    """Google Sheets にアクション（測定開始、停止、データ保存）を記録する"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    SHEET.append_row([timestamp, action, measurement_time, measurement_value])
    st.success(f"Action saved: {action}")

# 測定データを取得して表示
def get_data():
    data = SHEET.get_all_values()
    if len(data) > 1:
        df = pd.DataFrame(data[1:], columns=data[0])  # 1行目をヘッダーとして取得
        return df
    return pd.DataFrame()  # データがない場合、空の DataFrame を返す

# ボタンレイアウト
col1, col2 = st.columns(2)

with col1:
    if st.button("Stop Measurement"):
        save_data_to_google_sheets(action="Stop Measurement")
        st.success("Measurement Stopped")

with col2:
    if st.button("Stop Measurement & Save Data"):
        save_data_to_google_sheets(action="Stop and Save Data")
        st.success("Measurement Stopped & Data Saved")

if st.button("Start Measurement"):
    save_data_to_google_sheets(action="Start Measurement", measurement_time=M_time)
    st.success("Measurement Running...")
    
    for _ in range(M_time // 5):  # 5秒ごとにデータを記録
        measurement_value = 0.0  # 仮のデータ (実際の測定値を取得するロジックに変更)
        save_data_to_google_sheets(action="Measurement Data", measurement_value=measurement_value)
        time.sleep(5)

    st.success("Measurement Completed")

# 測定データの表示
st.subheader("Measurement Data")
df = get_data()
st.dataframe(df)


