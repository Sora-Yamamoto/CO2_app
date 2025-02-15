import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import time
import json

# ✅ **🔹 ここを最初に配置**（必ず一番上にする）
st.set_page_config(page_title="CO2 Sensor Application", layout="wide")

# Google Sheets API の認証
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Secrets から `credentials.json` の内容を取得（エラーハンドリング付き）
try:
    creds_json = json.loads(st.secrets["GOOGLE_CREDENTIALS"])
    CREDS = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, SCOPE)
    CLIENT = gspread.authorize(CREDS)
    st.success("✅ Google Sheets 認証に成功しました")
except Exception as e:
    st.error(f"❌ 認証に失敗しました: {e}")
    st.stop()

# Google Sheets の設定
SPREADSHEET_ID = "1-yaWx4l0AS44lAv9SUBqAQaxSyQqYCGQqEBsl1Zn_Zs"  # Google Sheets の ID
try:
    SHEET = CLIENT.open_by_key(SPREADSHEET_ID).sheet1  # 1枚目のシートを取得
    st.success("✅ Google Sheets への接続に成功しました")
except Exception as e:
    st.error(f"❌ Google Sheets の取得に失敗しました: {e}")
    st.stop()

# メイン関数
def main():
    # セッションステートの初期化
    for key, value in {
        "ser": None,
        "I_435nm_ave": 1.9497885376366615,
        "I_490nm_ave": 2.2112016069155542,
        "I_590nm_ave": 0.8408672705516362,
        "I_735nm_ave": 0.8317714985217586
    }.items():
        if key not in st.session_state:
            st.session_state[key] = value

    # タイトル
    st.title("CO2 Sensor Application")
    st.text("Google Sheets から取得したデータをリアルタイム表示")

    # データを取得して表示する関数（エラーハンドリング付き）
    def get_data():
        try:
            data = SHEET.get_all_values()  # Google Sheets からデータ取得
            if not data:  # データが空の場合
                st.warning("⚠️ Google Sheets にデータがありません")
                return pd.DataFrame(columns=["CO2濃度"])  # 空のDataFrameを返す
            df = pd.DataFrame(data, columns=["CO2濃度"])
            return df
        except Exception as e:
            st.error(f"❌ データの取得に失敗しました: {e}")
            return pd.DataFrame(columns=["CO2濃度"])  # エラー時も空のDataFrameを返す

    # データを定期的に更新
    placeholder = st.empty()
    while True:
        df = get_data()
        placeholder.dataframe(df)  # DataFrame を更新
        time.sleep(5)  # 5秒ごとに更新

# メイン関数を実行
if __name__ == "__main__":
    main()


