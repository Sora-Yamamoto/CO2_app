import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def visualize_intensity(intensity_data, chart_placeholder, is_pw=False):
    # Creating the Plotly chart for I_list data
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=intensity_data["Time"],
            y=intensity_data["I_435nm"],
            mode="lines+markers",
            name="I_435nm",
            line=dict(color="blue"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=intensity_data["Time"],
            y=intensity_data["I_490nm"],
            mode="lines+markers",
            name="I_490nm",
            line=dict(color="green"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=intensity_data["Time"],
            y=intensity_data["I_590nm"],
            mode="lines+markers",
            name="I_590nm",
            line=dict(color="orange"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=intensity_data["Time"],
            y=intensity_data["I_735nm"],
            mode="lines+markers",
            name="I_735nm",
            line=dict(color="red"),
        )
    )

    if is_pw:
        # 5つ以上のデータがある場合のみ線を引く
        if len(intensity_data) >= 5:
            # 最新データから5つ目のデータポイントを取得
            x_value_for_line = intensity_data["Time"].iloc[-5]

            # Y軸に平行な線を引く
            fig.add_shape(
                dict(
                    type="line",
                    x0=x_value_for_line,
                    y0=intensity_data[["I_435nm", "I_490nm", "I_590nm", "I_735nm"]].min().min(),
                    x1=x_value_for_line,
                    y1=intensity_data[["I_435nm", "I_490nm", "I_590nm", "I_735nm"]].max().max(),
                    line=dict(color="black", width=2, dash="dash"),
                )
            )

    fig.update_layout(
        title=dict(
            text="Intensity data",
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
                text="Intensity",  # y軸タイトルのテキスト
                font=dict(size=24),  # y軸タイトルのフォントサイズ
            ),
            tickfont=dict(size=20),  # y軸の目盛りラベルのフォントサイズ
        ),
    )
    chart_placeholder.plotly_chart(fig, use_container_width=True)


def visualize_pw_intensity(chart_placeholder):
    intensity_data = pd.DataFrame(
        {
            "Time": st.session_state.pw_time,
            "I_435nm": st.session_state.pw_I_435nm,
            "I_490nm": st.session_state.pw_I_490nm,
            "I_590nm": st.session_state.pw_I_590nm,
            "I_735nm": st.session_state.pw_I_735nm,
        }
    )
    is_pw = True
    visualize_intensity(intensity_data, chart_placeholder, is_pw)


def visualize_co2_intensity(chart_placeholder):
    intensity_data = pd.DataFrame(
        {
            "Time": st.session_state.co2_time,
            "I_435nm": st.session_state.co2_I_435nm,
            "I_490nm": st.session_state.co2_I_490nm,
            "I_590nm": st.session_state.co2_I_590nm,
            "I_735nm": st.session_state.co2_I_735nm,
        }
    )
    visualize_intensity(intensity_data, chart_placeholder)
