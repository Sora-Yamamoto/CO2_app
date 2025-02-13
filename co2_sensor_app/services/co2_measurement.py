import time

import streamlit as st
from services import (
    append_data_to_list,
    check_stable,
    initialize_data_list,
    make_date_folder,
    save_data_to_csv,
    save_data_to_image,
    slack_notification,
    visualize_A_R_data,
    visualize_abs_data,
    visualize_intensity_data,
    visualize_pco2_data,
    visualize_ref_data,
    visualize_sig_data,
)


def start_measurement_co2(M_time, ppm, stableCheck, measure_temp):
    print(f"測定温度: {measure_temp}°C で測定を開始")
    if st.session_state.ser and st.session_state.ser.is_open:
        # Measurement settings
        M_command = "JM"
        M_averageNumber = 10
        M_interval = 100
        M_delay = 5  # ここが1未満だと測定のプロット間隔がおかしくなる。おそらく制御基板側の仕様。
        M_text = f"{M_command}{M_averageNumber}, {M_interval}, {M_delay}, {M_time}\r"
        each_M_time = (M_averageNumber * M_interval * 5) / 1000  # 5
        plot_interval = each_M_time + M_delay
        # Number of values to check for CSV output
        values_num = 10

        # Initialize data
        initialize_data_list.initialize_co2_data()

        st.session_state.ser.write(M_text.encode("utf-8"))
        start_time = time.time()
        data = b""
        i = 0

        # Placeholders for Plotly charts
        colminus1, col0 = st.columns(2)
        pco2_chart_placeholder = colminus1.empty()
        A_R_chart_placeholder = col0.empty()
        col1, col2 = st.columns(2)
        abs_chart_placeholder = col1.empty()
        intensity_chart_placeholder = col2.empty()
        col3, col4 = st.columns(2)
        ref_chart_placeholder = col3.empty()
        sig_chart_placeholder = col4.empty()

        # Progress bar
        progress_bar = st.progress(0)

        while (time.time() - start_time) < M_time:
            one_byte = st.session_state.ser.read(1)
            data += one_byte
            if one_byte == b"\r":
                data = data.decode("utf-8")
                if data.startswith("F"):
                    time_for_plot = i * plot_interval
                    # Append data to lists
                    append_data_to_list.append_co2_data(data, time_for_plot)

                    # Update the Plotly chart for pco2 data
                    visualize_pco2_data.visualize_co2_pco2(pco2_chart_placeholder)

                    # Update the Plotly chart for A_R data
                    visualize_A_R_data.visualize_co2_A_R(A_R_chart_placeholder)
                    # Update the Plotly chart for absorbance data
                    visualize_abs_data.visualize_co2_abs(abs_chart_placeholder)
                    # Update the Plotly chart for intensity data
                    visualize_intensity_data.visualize_co2_intensity(intensity_chart_placeholder)
                    # Update the Plotly chart for ref data
                    visualize_ref_data.visualize_co2_ref(ref_chart_placeholder)
                    # Update the Plotly chart for sig data
                    visualize_sig_data.visualize_co2_sig(sig_chart_placeholder)

                    # Check stability
                    if stableCheck:
                        is_stable = check_stable.is_stable(values_num)
                        print(is_stable)
                        if is_stable:
                            break

                    i += 1

                data = b""  # Reset data

            # Update progress bar
            progress_text = "Operation in progress..."
            progress_value = min((time.time() - start_time) / M_time, 1.0)
            progress_bar.progress(progress_value, progress_text)

        # Update progress bar
        progress_bar.empty()

        # calculate the average of the last ten values for A_R
        A_R_ave = sum(st.session_state.co2_A_R[-values_num:]) / values_num
        # Send a Slack notification
        slack_notification.slack_co2(ppm, A_R_ave)

        # Save data
        make_date_folder.make_date_folder()
        output_df = save_data_to_csv.save_co2_csv(ppm)
        save_data_to_image.save_co2_image(output_df, ppm)

    else:
        st.error("Serial port not open. Please try again.")
