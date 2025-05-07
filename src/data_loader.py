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
from fastf1.api import get_stint_summary

def get_stints(session, driver_code):
    summary = get_stint_summary(session.session_key)
    driver_stints = summary[summary['Driver'] == driver_code]
    return driver_stints[['Stint', 'Compound', 'StartLap', 'EndLap']]

