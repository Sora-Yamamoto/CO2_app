import time

import streamlit as st
from services import (
    append_data_to_list,
    calculate_display_pw_I_ave,
    initialize_data_list,
    make_date_folder,
    save_data_to_csv,
    save_data_to_image,
    slack_notification,
    visualize_intensity_data,
    visualize_ref_data,
    visualize_sig_data,
)


def start_measurement_pure_water(M_time):
    if st.session_state.ser and st.session_state.ser.is_open:
        # Measurement settings
        M_command = "JM"
        M_averageNumber = 10
        M_interval = 100
        M_delay = 5  # ここが1未満だと測定のプロット間隔がおかしくなる。おそらく制御基板側の仕様。
        M_text = f"{M_command}{M_averageNumber}, {M_interval}, {M_delay}, {M_time}\r"
        each_M_time = (M_averageNumber * M_interval * 5) / 1000  # 5
        plot_interval = each_M_time + M_delay

        # Data initialization in session_state
        initialize_data_list.initialize_pw_data()

        st.session_state.ser.write(M_text.encode("utf-8"))
        start_time = time.time()
        data = b""
        i = 0

        # Create three columns for side-by-side layout
        col1, col2, col3 = st.columns(3)

        # Placeholders for Plotly charts in different columns
        chart_placeholder = col1.empty()
        ref_chart_placeholder = col2.empty()
        sig_chart_placeholder = col3.empty()

        # Progress bar
        progress_bar = st.progress(0)
        progress_text_placeholder = st.empty()

        while (time.time() - start_time) < M_time:
            one_byte = st.session_state.ser.read(1)
            data += one_byte
            if one_byte == b"\r":
                data = data.decode("utf-8")
                if data.startswith("F"):
                    time_for_plot = i * plot_interval
                    # Append data to lists
                    append_data_to_list.append_pw_data(data, time_for_plot)
                    # Update the Plotly chart for intensity data
                    visualize_intensity_data.visualize_pw_intensity(chart_placeholder)
                    # Update the Plotly chart for ref data
                    visualize_ref_data.visualize_pw_ref(ref_chart_placeholder)
                    # Update the Plotly chart for sig data
                    visualize_sig_data.visualize_pw_sig(sig_chart_placeholder)

                    i += 1

                data = b""  # Reset data

            # Update progress bar
            progress_value = min((time.time() - start_time) / M_time, 1.0)
            progress_bar.progress(progress_value)
            progress_text_placeholder.text("Operation in progress...")

        # Update progress bar
        progress_bar.empty()

        # Calculate the average of the last five values for each intensity list
        calculate_display_pw_I_ave.calculate_display_pw_I_ave()
        # Save data
        make_date_folder.make_date_folder()
        output_df = save_data_to_csv.save_pw_csv()
        image_path = save_data_to_image.save_pw_image(output_df)

        # Send a Slack notification
        slack_notification.slack_pw(image_path)

    else:
        st.error("Serial port not open. Please try again.")
