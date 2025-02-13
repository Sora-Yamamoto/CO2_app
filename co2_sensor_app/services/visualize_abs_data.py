import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def visualize_abs(abs_data: pd.DataFrame, abs_chart_placeholder):
    # Creating the Plotly chart for I_list data
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=abs_data["Time"],
            y=abs_data["A_435nm"],
            mode="lines+markers",
            name="A_435nm",
            line=dict(color="blue"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=abs_data["Time"],
            y=abs_data["A_490nm"],
            mode="lines+markers",
            name="A_490nm",
            line=dict(color="green"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=abs_data["Time"],
            y=abs_data["A_590nm"],
            mode="lines+markers",
            name="A_590nm",
            line=dict(color="orange"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=abs_data["Time"],
            y=abs_data["A_735nm"],
            mode="lines+markers",
            name="A_735nm",
            line=dict(color="red"),
        )
    )

    fig.update_layout(
        title=dict(
            text="Absorbance data",
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
                text="Absorbance",  # y軸タイトルのテキスト
                font=dict(size=24),  # y軸タイトルのフォントサイズ
            ),
            tickfont=dict(size=20),  # y軸の目盛りラベルのフォントサイズ
        ),
    )
    abs_chart_placeholder.plotly_chart(fig, use_container_width=True)


def visualize_co2_abs(abs_chart_placeholder):
    abs_data = pd.DataFrame(
        {
            "Time": st.session_state.co2_time,
            "A_435nm": st.session_state.co2_A_435nm,
            "A_490nm": st.session_state.co2_A_490nm,
            "A_590nm": st.session_state.co2_A_590nm,
            "A_735nm": st.session_state.co2_A_735nm,
        }
    )
    visualize_abs(abs_data, abs_chart_placeholder)
