import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def visualize_A_R(A_R_data: pd.DataFrame, A_R_chart_placeholder):
    # Creating the Plotly chart for I_list data
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=A_R_data["Time"], y=A_R_data["A_R"], mode="lines+markers", name="A_R", line=dict(color="blue")
        )
    )

    # 10つのデータを使ってA_Rの平均値を計算していることを示す線
    if len(A_R_data) >= 10:  # 10つ以上のデータがある場合のみ線を引く
        # 最新データから10つ目のデータポイントを取得
        x_value_for_line = A_R_data["Time"].iloc[-10]

        # Y軸に平行な線を引く
        fig.add_shape(
            dict(
                type="line",
                x0=x_value_for_line,
                y0=A_R_data["A_R"].min(),
                x1=x_value_for_line,
                y1=A_R_data["A_R"].max(),
                line=dict(color="black", width=2, dash="dash"),
            )
        )

    fig.update_layout(
        title=dict(
            text="Absorbance Ratio data",
            font=dict(size=30),  # タイトルのフォントサイズを設定
        ),
        autosize=True,
        xaxis=dict(
            title=dict(
                text="Time[s]",  # x軸タイトルのテキスト
                font=dict(size=24),  # x軸タイトルのフォントサイズ
            ),
            tickfont=dict(size=20),  # x軸の目盛りラベルのフォントサイズ
        ),
        yaxis=dict(
            title=dict(
                text="Absorbance Ratio",  # y軸タイトルのテキスト
                font=dict(size=24),  # y軸タイトルのフォントサイズ
            ),
            tickfont=dict(size=20),  # y軸の目盛りラベルのフォントサイズ
        ),
    )
    # fig.write_image("A_R_chart.png") # 機能しない
    A_R_chart_placeholder.plotly_chart(fig, use_container_width=True)


def visualize_co2_A_R(A_R_chart_placeholder):
    A_R_data = pd.DataFrame(
        {
            "Time": st.session_state.co2_time,
            "A_R": st.session_state.co2_A_R,
        }
    )
    visualize_A_R(A_R_data, A_R_chart_placeholder)
