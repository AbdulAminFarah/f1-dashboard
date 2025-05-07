import streamlit as st
from src.data_loader import load_race_session, get_driver_laps, get_stints
from src.plot_utils import plot_lap_times, plot_stint_strategy

st.set_page_config(layout="wide")
st.title("🏎️ F1 Race Analytics Dashboard")

# Sidebar input
st.sidebar.header("Race Selection")
year = st.sidebar.selectbox("Year", list(range(2018, 2024))[::-1])
gp = st.sidebar.text_input("Grand Prix", "Monza")
driver1 = st.sidebar.text_input("Driver 1 Code", "VER")
driver2 = st.sidebar.text_input("Driver 2 Code", "HAM")

if st.sidebar.button("Load Session"):
    with st.spinner("Loading race data..."):
        session = load_race_session(year, gp)

        # Load driver laps
        laps1 = get_driver_laps(session, driver1)
        laps2 = get_driver_laps(session, driver2)

        # Plot lap times
        st.subheader(f"Lap Time Comparison: {driver1} vs {driver2}")
        fig1 = plot_lap_times(laps1, laps2, driver1, driver2)
        st.plotly_chart(fig1, use_container_width=True)

        # Stint plots
        stints1 = get_stints(session, driver1)
        stints2 = get_stints(session, driver2)

        st.subheader("Tyre Strategy")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"**{driver1}**")
            fig2 = plot_stint_strategy(stints1, driver1)
            st.plotly_chart(fig2, use_container_width=True)

        with col2:
            st.markdown(f"**{driver2}**")
            fig3 = plot_stint_strategy(stints2, driver2)
            st.plotly_chart(fig3, use_container_width=True)

        # Optional summary tables
        with st.expander("Stint Summary Tables"):
            st.write(f"**{driver1}**")
            st.dataframe(stints1)
            st.write(f"**{driver2}**")
            st.dataframe(stints2)
