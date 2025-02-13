import requests
import streamlit as st


def send_slack_notification(message, image_path=None):
    # image_pathでローカルの画像を送ろうとしたが、うまくいかず。後日、修正予定。
    SLACK_API_URL = "https://slack.com/api/chat.postMessage"
    SLACK_TOKEN = "xoxb-1042979646966-7406288794145-0xOdMZ4AX8Nyd6VRbqOP7OMZ"
    SLACK_CHANNEL = "test"

    headers = {"Authorization": f"Bearer {SLACK_TOKEN}", "Content-Type": "application/json"}
    payload = {"channel": SLACK_CHANNEL, "text": message}
    response = requests.post(SLACK_API_URL, headers=headers, json=payload)

    # Parse the JSON response
    response_data = response.json()

    if response_data.get("ok"):
        st.success("Notification sent successfully!")
    else:
        st.error(f"Failed to send notification: {response_data.get('error')}")


def slack_pw(image_path):
    message = f"""
        Pure water measurement completed.
        I_435nm_ave: {st.session_state.I_435nm_ave:.3f}
        I_490nm_ave: {st.session_state.I_490nm_ave:.3f}
        I_590nm_ave: {st.session_state.I_590nm_ave:.3f}
        I_735nm_ave: {st.session_state.I_735nm_ave:.3f}
        """
    send_slack_notification(message, image_path)


def slack_co2(ppm, A_R_ave):
    message = f"co2 measurement completed. {ppm}, A_R_ave: {A_R_ave:.3f}, {st.session_state.co2_time[-1]}s"
    send_slack_notification(message)
