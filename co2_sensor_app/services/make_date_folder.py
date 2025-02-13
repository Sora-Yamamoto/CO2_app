import os
import time


def make_date_folder():
    # 今日の日付を取得、日付をフォルダ名として使う
    folder_name = time.strftime("%Y%m%d")

    # フォルダの絶対パスを指定
    folder_path = f"data/date/{folder_name}"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"フォルダ | {folder_name} を作成しました")
    else:
        print(f"フォルダ | {folder_name} は既に存在します")
