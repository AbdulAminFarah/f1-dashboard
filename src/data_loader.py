import fastf1
import pandas as pd

fastf1.Cache.enable_cache('data/fastf1_cache')

def load_race_session(year, gp, session_type='R'):
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    return session

def get_driver_laps(session, driver_code):
    laps = session.laps.pick_driver(driver_code).pick_quicklaps()
    return laps[['LapNumber', 'LapTime', 'Compound', 'PitOutTime', 'PitInTime']]

#  Add get_stints()
def get_stints(session, driver_code):
    """Return tyre stint data for a driver."""
    driver_laps = session.laps.pick_driver(driver_code)
    stints = driver_laps.get_stint_info()
    return stints[['Stint', 'Compound', 'StartLap', 'EndLap']]
