import numpy as np
import streamlit as st
from services import serial_service


def is_stable(values_num):
    if len(st.session_state.co2_A_R) >= values_num:
        last_values = st.session_state.co2_A_R[-values_num:]
        std_dev = np.std(last_values)  # 標準偏差を計算
        A_R_ave = sum(last_values) / values_num
        st.write(f"Std Dev: {std_dev:.3f}, A_R_ave: {A_R_ave:.3f}")
        if std_dev <= 0.01:
            serial_service.stop_pump1()
            return True
        else:
            return False
    else:
        return False
