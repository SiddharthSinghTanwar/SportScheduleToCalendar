import fastf1
from ics import Calendar, Event
from datetime import datetime
import pandas as pd
import os

# 1. Setup Cache (FastF1 requires this to avoid re-downloading data)
os.makedirs('f1_cache', exist_ok=True)
fastf1.Cache.enable_cache('f1_cache')

def generate_f1_calendar(year=2026):
    print(f"Fetching {year} schedule...")
    schedule = fastf1.get_event_schedule(year)
    
    cal = Calendar()
    
    # We loop through each row in the schedule (each Grand Prix/Testing event)
    for _, event in schedule.iterrows():
        event_name = event['OfficialEventName']
        
        # FastF1 events have up to 5 sessions (P1, P2, P3, Quali, Race)
        # We check Session1 through Session5
        for i in range(1, 6):
            session_name = event[f'Session{i}']
            session_date = event[f'Session{i}DateUtc']
            
            # Only add if a date exists (some events have fewer sessions)
            if pd.notna(session_date):
                e = Event()
                e.name = f"F1: {event_name} - {session_name}"
                e.begin = session_date
                e.duration = {"hours": 1.5} # Standard session length estimate
                e.description = f"Location: {event['Location']}, {event['Country']}"
                cal.events.add(e)
                
    # Save to file
    filename = f"F1_{year}_Schedule.ics"
    with open(filename, 'w') as f:
        f.writelines(cal.serialize_iter())
    
    print(f"Successfully created {filename}")

if __name__ == "__main__":
    generate_f1_calendar(2026)