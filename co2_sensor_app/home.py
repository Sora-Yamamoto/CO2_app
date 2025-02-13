import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import time

# Google Sheets API の認証
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPE)
CLIENT = gspread.authorize(CREDS)

# Google Sheets の設定
SPREADSHEET_ID = "1-yaWx4l0AS44lAv9SUBqAQaxSyQqYCGQqEBsl1Zn_Zs"  # Google Sheets の ID
SHEET = CLIENT.open_by_key(SPREADSHEET_ID).sheet1  # 1枚目のシートを取得

# メイン関数
def main():
    st.set_page_config(page_title="My Custom App", layout="wide")

    # Initialize Streamlit session state
    if "ser" not in st.session_state:
        st.session_state.ser = None

    if "I_435nm_ave" not in st.session_state:
        st.session_state.I_435nm_ave = 1.9497885376366615
    if "I_490nm_ave" not in st.session_state:
        st.session_state.I_490nm_ave = 2.2112016069155542
    if "I_590nm_ave" not in st.session_state:
        st.session_state.I_590nm_ave = 0.8408672705516362
    if "I_735nm_ave" not in st.session_state:
        st.session_state.I_735nm_ave = 0.8317714985217586

    # タイトル
    st.title("CO2 Sensor Application")
    st.text("Google Sheets から取得したデータをリアルタイム表示")

    # データを取得して表示する関数
    def get_data():
        data = SHEET.get_all_values()  # Google Sheets からデータ取得
        df = pd.DataFrame(data, columns=["CO2濃度"])
        return df

    # データを定期的に更新
    placeholder = st.empty()
    while True:
        df = get_data()
        placeholder.dataframe(df)  # DataFrame を更新
        time.sleep(5)  # 5秒ごとに更新

# メイン関数を実行
if __name__ == "__main__":
    main()

