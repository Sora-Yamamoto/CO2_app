import serial
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API の認証
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# credentials.json のフルパスを指定！（変更）
CREDENTIALS_PATH = "C:\\Users\\yanag\\CO2測定モニター\\co2_sensor_app\\credentials.json"

CREDS = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, SCOPE)
CLIENT = gspread.authorize(CREDS)

# Google Sheets の設定
SPREADSHEET_ID = "1-yaWx4l0AS44lAv9SUBqAQaxSyQqYCGQqEBsl1Zn_Zs"  # Google Sheets の ID
SHEET = CLIENT.open_by_key(SPREADSHEET_ID).sheet1  # 1枚目のシートを取得

# COM7 のシリアル通信を開く
try:
    ser = serial.Serial("COM7", baudrate=19200, timeout=1)
    print("COM7 に接続しました。データを読み取り中...")
except serial.SerialException as e:
    print(f"シリアルポートのオープンに失敗しました: {e}")
    ser = None  # エラーが発生した場合、ser を None にする

# メインのループ
if ser:  # COMポートが開いている場合のみ実行
    while True:
        try:
            data = ser.readline().decode().strip()
            if data:
                print(f"送信中: {data}")
                SHEET.append_row([data])  # Google Sheets にデータを追加
        except Exception as e:
            print(f"データの送信中にエラーが発生しました: {e}")
else:
    print("シリアル通信が開けないため、データ送信を中止します。")
