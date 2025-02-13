import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def visualize_ref(ref_data, ref_chart_placeholder):
    # Creating the Plotly chart for ref_list data
    ref_fig = go.Figure()
    ref_fig.add_trace(
        go.Scatter(
            x=ref_data["Time"],
            y=ref_data["Ref_dark"],
            mode="lines+markers",
            name="Ref_dark",
            line=dict(color="black"),
        )
    )
    ref_fig.add_trace(
        go.Scatter(
            x=ref_data["Time"],
            y=ref_data["Ref_435nm"],
            mode="lines+markers",
            name="Ref_435nm",
            line=dict(color="blue"),
        )
    )
    ref_fig.add_trace(
        go.Scatter(
            x=ref_data["Time"],
            y=ref_data["Ref_490nm"],
            mode="lines+markers",
            name="Ref_490nm",
            line=dict(color="green"),
        )
    )
    ref_fig.add_trace(
        go.Scatter(
            x=ref_data["Time"],
            y=ref_data["Ref_590nm"],
            mode="lines+markers",
            name="Ref_590nm",
            line=dict(color="orange"),
        )
    )
    ref_fig.add_trace(
        go.Scatter(
            x=ref_data["Time"],
            y=ref_data["Ref_735nm"],
            mode="lines+markers",
            name="Ref_735nm",
            line=dict(color="red"),
        )
    )

    ref_fig.update_layout(
        title=dict(
            text="Reference raw data",
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
                text="Reference Intensity",  # y軸タイトルのテキスト
                font=dict(size=24),  # y軸タイトルのフォントサイズ
            ),
            tickfont=dict(size=20),  # y軸の目盛りラベルのフォントサイズ
        ),
    )
    ref_chart_placeholder.plotly_chart(ref_fig, use_container_width=True)


def visualize_pw_ref(ref_chart_placeholder):
    ref_data = pd.DataFrame(
        {
            "Time": st.session_state.pw_time,
            "Ref_dark": st.session_state.pw_ref_dark,
            "Ref_435nm": st.session_state.pw_ref_435nm,
            "Ref_490nm": st.session_state.pw_ref_490nm,
            "Ref_590nm": st.session_state.pw_ref_590nm,
            "Ref_735nm": st.session_state.pw_ref_735nm,
        }
    )
    visualize_ref(ref_data, ref_chart_placeholder)


def visualize_co2_ref(ref_chart_placeholder):
    ref_data = pd.DataFrame(
        {
            "Time": st.session_state.co2_time,
            "Ref_dark": st.session_state.co2_ref_dark,
            "Ref_435nm": st.session_state.co2_ref_435nm,
            "Ref_490nm": st.session_state.co2_ref_490nm,
            "Ref_590nm": st.session_state.co2_ref_590nm,
            "Ref_735nm": st.session_state.co2_ref_735nm,
        }
    )
    visualize_ref(ref_data, ref_chart_placeholder)
