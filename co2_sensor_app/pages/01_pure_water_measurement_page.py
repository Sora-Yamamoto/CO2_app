import streamlit as st
from services import make_date_folder, save_data_to_csv, save_data_to_image, serial_service
from services.pure_water_measurement import start_measurement_pure_water


st.title("Pure Water Measurement")

# Define a default value for M_time
default_time = 300

# custom CSS
st.markdown(
    """
<style>
    .big-font {
        font-size: 24px !important;
    }
    .red-text {
        color: red;
        font-weight: bold;
    }
</style>
""",
    unsafe_allow_html=True,
)

M_time = st.slider(
    "Quick Set Measurement Time (seconds)", min_value=10, max_value=1000, value=default_time, step=10
)

st.markdown(
    f'<p class="big-font">Selected time: <span class="red-text">{M_time}</span> seconds</p>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Stop Measurement"):
        serial_service.stop_pump1()
        st.success("Measurement Stopped")

with col2:
    if st.button("Stop Measurement & save data"):
        serial_service.stop_pump1()
        make_date_folder.make_date_folder()
        output_df = save_data_to_csv.save_pw_csv()
        save_data_to_image.save_pw_image(output_df)
        st.success("Measurement Stopped")

if st.button("Start Measurement"):
    st.success("Measurement Running")
    start_measurement_pure_water(M_time)
    st.success("Measurement Completed")
