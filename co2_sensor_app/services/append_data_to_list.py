import numpy as np
import streamlit as st


def append_pw_data(data, time_for_plot):
    st.session_state.pw_year.append(int(data[1:5], 16))
    st.session_state.pw_month.append(int(data[5:7], 16))
    st.session_state.pw_day.append(int(data[7:9], 16))
    st.session_state.pw_hour.append(int(data[9:11], 16))
    st.session_state.pw_minute.append(int(data[11:13], 16))
    st.session_state.pw_second.append(int(data[13:15], 16))
    st.session_state.pw_state.append(int(data[15:17], 16))
    st.session_state.pw_sig_dark.append(int(data[17:21], 16))
    st.session_state.pw_sig_435nm.append(int(data[21:25], 16))
    st.session_state.pw_sig_490nm.append(int(data[25:29], 16))
    st.session_state.pw_sig_590nm.append(int(data[29:33], 16))
    st.session_state.pw_sig_735nm.append(int(data[33:37], 16))
    st.session_state.pw_ref_dark.append(int(data[37:41], 16))
    st.session_state.pw_ref_435nm.append(int(data[41:45], 16))
    st.session_state.pw_ref_490nm.append(int(data[45:49], 16))
    st.session_state.pw_ref_590nm.append(int(data[49:53], 16))
    st.session_state.pw_ref_735nm.append(int(data[53:57], 16))
    st.session_state.pw_measurement_number.append(int(data[61:65], 16))

    # Calculated data
    st.session_state.pw_time.append(time_for_plot)
    st.session_state.pw_I_435nm.append(
        (st.session_state.pw_sig_435nm[-1] - st.session_state.pw_sig_dark[-1])
        / (st.session_state.pw_ref_435nm[-1] - st.session_state.pw_ref_dark[-1])
    )
    st.session_state.pw_I_490nm.append(
        (st.session_state.pw_sig_490nm[-1] - st.session_state.pw_sig_dark[-1])
        / (st.session_state.pw_ref_490nm[-1] - st.session_state.pw_ref_dark[-1])
    )
    st.session_state.pw_I_590nm.append(
        (st.session_state.pw_sig_590nm[-1] - st.session_state.pw_sig_dark[-1])
        / (st.session_state.pw_ref_590nm[-1] - st.session_state.pw_ref_dark[-1])
    )
    st.session_state.pw_I_735nm.append(
        (st.session_state.pw_sig_735nm[-1] - st.session_state.pw_sig_dark[-1])
        / (st.session_state.pw_ref_735nm[-1] - st.session_state.pw_ref_dark[-1])
    )


def append_co2_data(data, time_for_plot):
    """CO₂ 測定データを解析し、pCO₂ を計算して session_state に保存"""

    # `st.session_state.measure_temp` が未定義ならデフォルト値 25 を設定
    if "measure_temp" not in st.session_state:
        st.session_state.measure_temp = 25.0  # デフォルト 25℃

    T = st.session_state.measure_temp  # 測定時の温度を session_state から取得

    st.session_state.co2_year.append(int(data[1:5], 16))
    st.session_state.co2_month.append(int(data[5:7], 16))
    st.session_state.co2_day.append(int(data[7:9], 16))
    st.session_state.co2_hour.append(int(data[9:11], 16))
    st.session_state.co2_minute.append(int(data[11:13], 16))
    st.session_state.co2_second.append(int(data[13:15], 16))
    st.session_state.co2_state.append(int(data[15:17], 16))
    st.session_state.co2_sig_dark.append(int(data[17:21], 16))
    st.session_state.co2_sig_435nm.append(int(data[21:25], 16))
    st.session_state.co2_sig_490nm.append(int(data[25:29], 16))
    st.session_state.co2_sig_590nm.append(int(data[29:33], 16))
    st.session_state.co2_sig_735nm.append(int(data[33:37], 16))
    st.session_state.co2_ref_dark.append(int(data[37:41], 16))
    st.session_state.co2_ref_435nm.append(int(data[41:45], 16))
    st.session_state.co2_ref_490nm.append(int(data[45:49], 16))
    st.session_state.co2_ref_590nm.append(int(data[49:53], 16))
    st.session_state.co2_ref_735nm.append(int(data[53:57], 16))
    st.session_state.co2_measurement_number.append(int(data[61:65], 16))

    # Calculated data
    st.session_state.co2_time.append(time_for_plot)
    st.session_state.co2_I_435nm.append(
        (st.session_state.co2_sig_435nm[-1] - st.session_state.co2_sig_dark[-1])
        / (st.session_state.co2_ref_435nm[-1] - st.session_state.co2_ref_dark[-1])
    )
    st.session_state.co2_I_490nm.append(
        (st.session_state.co2_sig_490nm[-1] - st.session_state.co2_sig_dark[-1])
        / (st.session_state.co2_ref_490nm[-1] - st.session_state.co2_ref_dark[-1])
    )
    st.session_state.co2_I_590nm.append(
        (st.session_state.co2_sig_590nm[-1] - st.session_state.co2_sig_dark[-1])
        / (st.session_state.co2_ref_590nm[-1] - st.session_state.co2_ref_dark[-1])
    )
    st.session_state.co2_I_735nm.append(
        (st.session_state.co2_sig_735nm[-1] - st.session_state.co2_sig_dark[-1])
        / (st.session_state.co2_ref_735nm[-1] - st.session_state.co2_ref_dark[-1])
    )

    st.session_state.co2_A_435nm.append(
        -np.log10((st.session_state.co2_I_435nm[-1] / st.session_state.I_435nm_ave))
    )
    st.session_state.co2_A_490nm.append(
        -np.log10((st.session_state.co2_I_490nm[-1] / st.session_state.I_490nm_ave))
    )
    st.session_state.co2_A_590nm.append(
        -np.log10((st.session_state.co2_I_590nm[-1] / st.session_state.I_590nm_ave))
    )
    st.session_state.co2_A_735nm.append(
        -np.log10((st.session_state.co2_I_735nm[-1] / st.session_state.I_735nm_ave))
    )
    st.session_state.co2_A_R.append(
        (st.session_state.co2_A_590nm[-1] - st.session_state.co2_A_735nm[-1])
        / (st.session_state.co2_A_435nm[-1] - st.session_state.co2_A_735nm[-1])
    )

    # ★ pCO₂ の計算を追加 ★
    e_1 = 0.00387
    e_2 = 2.858
    e_3 = 0.0181
    R_CO2 = -np.log10((st.session_state.co2_A_R[-1] - e_1) / (e_2 - e_3 * st.session_state.co2_A_R[-1]))

    CalT = 25  # 校正時の温度
    TCoef = (-0.0081437 - 0.0039777 * ((T - CalT) * 0.008 + R_CO2) + 0.0032873 * ((T - CalT) * 0.008 + R_CO2))
    TR_CO2 = (T - CalT) * (-TCoef) + R_CO2

    a = 0.094427
    b = 0.327151
    c = -1.64669
    pCO2 = 10 ** ((-1 * b + (b**2 - (4 * a * (c - TR_CO2))) ** 0.5) / (2 * a))

    if "co2_pCO2" not in st.session_state:
        st.session_state.co2_pCO2 = []  # 初期化

    st.session_state.co2_pCO2.append(pCO2)  # ここでエラーにならない    
