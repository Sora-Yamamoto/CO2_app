import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def calc_TCoef(T, R_CO2):
    """温度補正係数 TCoef を計算"""
    CalT = 25  # 校正時の温度（固定値）
    return (-0.0081437 - 0.0039777 * ((T - CalT) * 0.008 + R_CO2) + 0.0032873 * ((T - CalT) * 0.008 + R_CO2))


def calc_TR_co2(T, R_CO2):
    """温度補正した R_CO2 (TR_CO2) を計算"""
    TCoef = calc_TCoef(T, R_CO2)
    CalT = 25  # 校正時の温度（固定値）
    return (T - CalT) * (-TCoef) + R_CO2


def calc_R_co2(A_R):
    """A_R から R_CO2 を計算"""
    e_1 = 0.00387
    e_2 = 2.858
    e_3 = 0.0181
    return -np.log10((A_R - e_1) / (e_2 - e_3 * A_R))


def calc_pCO2(A_R, T):
    """温度補正後の R_CO2 を使って pCO2 を計算"""
    R_CO2 = calc_R_co2(A_R)
    TR_CO2 = calc_TR_co2(T, R_CO2)

    # 機器固定値（理論値）
    a = 0.094427
    b = 0.327151
    c = -1.64669

    # pCO2 の 2 次方程式を解く
    pCO2 = 10 ** ((-1 * b + (b**2 - (4 * a * (c - TR_CO2))) ** 0.5) / (2 * a))
    return pCO2


def _visualize_pco2(A_R_data: pd.DataFrame, T, pco2_chart_placeholder):
    """A_R データから pCO2 を計算し、グラフを作成"""
    pco2 = calc_pCO2(A_R_data["A_R"], T)

    # Plotly でグラフ作成
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=A_R_data["Time"], y=pco2, mode="lines+markers", name="pCO2", line=dict(color="blue"))
    )

    # 最新10データの境界線
    if len(A_R_data) >= 10:
        x_value_for_line = A_R_data["Time"].iloc[-10]
        fig.add_shape(
            dict(
                type="line",
                x0=x_value_for_line,
                y0=pco2.min(),
                x1=x_value_for_line,
                y1=pco2.max(),
                line=dict(color="black", width=2, dash="dash"),
            )
        )

    fig.update_layout(
        title=dict(text="pCO₂ Data", font=dict(size=30)),
        autosize=True,
        xaxis=dict(title=dict(text="Time[s]", font=dict(size=24)), tickfont=dict(size=20)),
        yaxis=dict(title=dict(text="pCO₂", font=dict(size=24)), tickfont=dict(size=20)),
    )

    pco2_chart_placeholder.plotly_chart(fig, use_container_width=True)


def visualize_co2_pco2(pco2_chart_placeholder):
    """Streamlit で A_R データを取得して pCO2 を可視化"""
    A_R_data = pd.DataFrame(
        {
            "Time": st.session_state.co2_time,
            "A_R": st.session_state.co2_A_R,
        }
    )

    # 測定時の温度を取得
    T = st.session_state.measure_temp  # 測定時の温度

    _visualize_pco2(A_R_data, T, pco2_chart_placeholder)
