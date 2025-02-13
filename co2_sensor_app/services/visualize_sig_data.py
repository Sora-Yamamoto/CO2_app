import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def visualize_sig(sig_data, sig_chart_placeholder):
    # Creating the Plotly chart for sig_list data
    sig_fig = go.Figure()
    sig_fig.add_trace(
        go.Scatter(
            x=sig_data["Time"],
            y=sig_data["Sig_dark"],
            mode="lines+markers",
            name="Sig_dark",
            line=dict(color="black"),
        )
    )
    sig_fig.add_trace(
        go.Scatter(
            x=sig_data["Time"],
            y=sig_data["Sig_435nm"],
            mode="lines+markers",
            name="Sig_435nm",
            line=dict(color="blue"),
        )
    )
    sig_fig.add_trace(
        go.Scatter(
            x=sig_data["Time"],
            y=sig_data["Sig_490nm"],
            mode="lines+markers",
            name="Sig_490nm",
            line=dict(color="green"),
        )
    )
    sig_fig.add_trace(
        go.Scatter(
            x=sig_data["Time"],
            y=sig_data["Sig_590nm"],
            mode="lines+markers",
            name="Sig_590nm",
            line=dict(color="orange"),
        )
    )
    sig_fig.add_trace(
        go.Scatter(
            x=sig_data["Time"],
            y=sig_data["Sig_735nm"],
            mode="lines+markers",
            name="Sig_735nm",
            line=dict(color="red"),
        )
    )

    sig_fig.update_layout(
        title=dict(
            text="Signal raw data",
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
                text="Signal Intensity",  # y軸タイトルのテキスト
                font=dict(size=24),  # y軸タイトルのフォントサイズ
            ),
            tickfont=dict(size=20),  # y軸の目盛りラベルのフォントサイズ
        ),
    )
    sig_chart_placeholder.plotly_chart(sig_fig, use_container_width=True)


def visualize_pw_sig(sig_chart_placeholder):
    sig_data = pd.DataFrame(
        {
            "Time": st.session_state.pw_time,
            "Sig_dark": st.session_state.pw_sig_dark,
            "Sig_435nm": st.session_state.pw_sig_435nm,
            "Sig_490nm": st.session_state.pw_sig_490nm,
            "Sig_590nm": st.session_state.pw_sig_590nm,
            "Sig_735nm": st.session_state.pw_sig_735nm,
        }
    )
    visualize_sig(sig_data, sig_chart_placeholder)


def visualize_co2_sig(sig_chart_placeholder):
    sig_data = pd.DataFrame(
        {
            "Time": st.session_state.co2_time,
            "Sig_dark": st.session_state.co2_sig_dark,
            "Sig_435nm": st.session_state.co2_sig_435nm,
            "Sig_490nm": st.session_state.co2_sig_490nm,
            "Sig_590nm": st.session_state.co2_sig_590nm,
            "Sig_735nm": st.session_state.co2_sig_735nm,
        }
    )
    visualize_sig(sig_data, sig_chart_placeholder)
