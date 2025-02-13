import time

import polars as pl
import streamlit as st
from services import initialize_data_list


def save_pw_csv():
    # Save data to CSV
    data_dict = {
        "Year": st.session_state.pw_year,
        "Month": st.session_state.pw_month,
        "Day": st.session_state.pw_day,
        "Hour": st.session_state.pw_hour,
        "Minute": st.session_state.pw_minute,
        "Second": st.session_state.pw_second,
        "State": st.session_state.pw_state,
        "Sig_Dark": st.session_state.pw_sig_dark,
        "Sig_435nm": st.session_state.pw_sig_435nm,
        "Sig_490nm": st.session_state.pw_sig_490nm,
        "Sig_590nm": st.session_state.pw_sig_590nm,
        "Sig_735nm": st.session_state.pw_sig_735nm,
        "Ref_Dark": st.session_state.pw_ref_dark,
        "Ref_435nm": st.session_state.pw_ref_435nm,
        "Ref_490nm": st.session_state.pw_ref_490nm,
        "Ref_590nm": st.session_state.pw_ref_590nm,
        "Ref_735nm": st.session_state.pw_ref_735nm,
        "Measurement_Number": st.session_state.pw_measurement_number,
        "Time": st.session_state.pw_time,
        "I_435nm": st.session_state.pw_I_435nm,
        "I_490nm": st.session_state.pw_I_490nm,
        "I_590nm": st.session_state.pw_I_590nm,
        "I_735nm": st.session_state.pw_I_735nm,
    }
    formatted_time = time.strftime("%Y%m%d_%H%M", time.localtime())
    date_folder_name = time.strftime("%Y%m%d", time.localtime())
    # Create Polars DataFrame
    output_df = pl.DataFrame(data_dict)
    if output_df.is_empty():
        print("The DataFrame is empty. No csv was saved.")
    else:
        # Save to CSV
        output_df.write_csv(f"data/type/pw_csv/{formatted_time}_pw.csv")
        output_df.write_csv(f"data/date/{date_folder_name}/{formatted_time}_pw.csv")
    # Data initialization in session_state
    initialize_data_list.initialize_pw_data()
    return output_df


def save_co2_csv(ppm):
    # Save data to CSV
    data_dict = {
        "Year": st.session_state.co2_year,
        "Month": st.session_state.co2_month,
        "Day": st.session_state.co2_day,
        "Hour": st.session_state.co2_hour,
        "Minute": st.session_state.co2_minute,
        "Second": st.session_state.co2_second,
        "State": st.session_state.co2_state,
        "Sig_Dark": st.session_state.co2_sig_dark,
        "Sig_435nm": st.session_state.co2_sig_435nm,
        "Sig_490nm": st.session_state.co2_sig_490nm,
        "Sig_590nm": st.session_state.co2_sig_590nm,
        "Sig_735nm": st.session_state.co2_sig_735nm,
        "Ref_Dark": st.session_state.co2_ref_dark,
        "Ref_435nm": st.session_state.co2_ref_435nm,
        "Ref_490nm": st.session_state.co2_ref_490nm,
        "Ref_590nm": st.session_state.co2_ref_590nm,
        "Ref_735nm": st.session_state.co2_ref_735nm,
        "Measurement_Number": st.session_state.co2_measurement_number,
        "Time": st.session_state.co2_time,
        "I_435nm": st.session_state.co2_I_435nm,
        "I_490nm": st.session_state.co2_I_490nm,
        "I_590nm": st.session_state.co2_I_590nm,
        "I_735nm": st.session_state.co2_I_735nm,
        "A_435nm": st.session_state.co2_A_435nm,
        "A_490nm": st.session_state.co2_A_490nm,
        "A_590nm": st.session_state.co2_A_590nm,
        "A_735nm": st.session_state.co2_A_735nm,
        "A_R": st.session_state.co2_A_R,
        "pCO2": st.session_state.co2_pCO2,
    }

    # 各データの長さを確認
    print("データの長さ:")
    for key, value in data_dict.items():
        if isinstance(value, list):
            print(f"{key}: {len(value)}")

    # 各データの最大長を取得
    max_length = max(len(v) if isinstance(v, list) else 1 for v in data_dict.values())

    # 各データの長さを max_length に統一
    for key, value in data_dict.items():
        if isinstance(value, list):
            if len(value) == 1:
                data_dict[key] = value * max_length  # 1要素のリストを拡張
            elif len(value) < max_length:
                data_dict[key] += [value[-1]] * (max_length - len(value))  # 最後の要素をコピー

    # 長さが統一されたことを確認
    lengths = {key: len(value) if isinstance(value, list) else 1 for key, value in data_dict.items()}
    if len(set(lengths.values())) != 1:
        raise ValueError(f"データの長さが不一致です: {lengths}")

    formatted_time = time.strftime("%Y%m%d_%H%M", time.localtime())
    date_folder_name = time.strftime("%Y%m%d", time.localtime())

    # DataFrame 作成
    output_df = pl.DataFrame(data_dict)
    if output_df.is_empty():
        print("The DataFrame is empty. No csv was saved.")
    else:
        # CSV に保存
        output_df.write_csv(f"data/type/co2_csv/{formatted_time}_{ppm}_co2.csv")
        output_df.write_csv(f"data/date/{date_folder_name}/{formatted_time}_{ppm}_co2.csv")

    # データ初期化
    initialize_data_list.initialize_co2_data()
    return output_df

