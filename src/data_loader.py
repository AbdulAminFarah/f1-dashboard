import fastf1
import pandas as pd

# Enable FastF1 cache
fastf1.Cache.enable_cache('data/fastf1_cache')


def load_race_session(year, gp, session_type='R'):
    """Loads a race session given year, Grand Prix name, and session type."""
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    return session


def get_driver_laps(session, driver_code):
    """Returns clean laps for a specific driver."""
    laps = session.laps.pick_driver(driver_code).pick_quicklaps()
    return laps[['LapNumber', 'LapTime', 'Compound', 'PitOutTime', 'PitInTime']]


def get_stints(session, driver_code):
    """Compute tyre stints by detecting compound changes from lap data."""
    driver_laps = session.laps.pick_driver(driver_code)
    driver_laps = driver_laps[["LapNumber", "Compound"]].reset_index(drop=True)

    stints = []
    current_compound = None
    start_lap = None

    for idx, row in driver_laps.iterrows():
        compound = row['Compound']
        lap = row['LapNumber']

        if compound != current_compound:
            if current_compound is not None:
                stints.append({
                    "Stint": len(stints) + 1,
                    "Compound": current_compound,
                    "StartLap": start_lap,
                    "EndLap": lap - 1
                })
            current_compound = compound
            start_lap = lap

    if current_compound is not None:
        stints.append({
            "Stint": len(stints) + 1,
            "Compound": current_compound,
            "StartLap": start_lap,
            "EndLap": driver_laps["LapNumber"].iloc[-1]
        })

    return pd.DataFrame(stints)
