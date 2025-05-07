import streamlit as st
from src.data_loader import load_race_session, get_driver_laps
from src.plot_utils import plot_lap_times

st.set_page_config(page_title="F1 Analytics Dashboard", layout="wide")
st.title("🏁 F1 Lap Time Comparison Dashboard")

year = st.sidebar.selectbox("Year", [2023, 2022, 2021])
gp = st.sidebar.selectbox("Grand Prix", ["Silverstone", "Monza", "Spa", "Suzuka"])
driver1 = st.sidebar.text_input("Driver 1 Code", "VER")
driver2 = st.sidebar.text_input("Driver 2 Code", "HAM")

if st.sidebar.button("Load"):
    with st.spinner("Loading session data..."):
        session = load_race_session(year, gp)
        laps1 = get_driver_laps(session, driver1)
        laps2 = get_driver_laps(session, driver2)

        fig1 = plot_lap_times(laps1, driver1, 'red')
        fig2 = plot_lap_times(laps2, driver2, 'blue')

        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)

        # Get stint data and plot
        stints1 = get_stints(session, driver1)
        stints2 = get_stints(session, driver2)

        fig3 = plot_stint_strategy(stints1, driver1, 'red')
        fig4 = plot_stint_strategy(stints2, driver2, 'blue')

        st.subheader(f"Tyre Strategy: {driver1} vs {driver2}")
        st.plotly_chart(fig3, use_container_width=True)
        st.plotly_chart(fig4, use_container_width=True)
