from api import fetch_latest_race, fetch_drivers, fetch_session_results, fetch_race_control
from analyzer import analyze_race_control

def main():
    # Fetch the latest race
    race = fetch_latest_race()

    # Fetch all drivers for that race
    drivers = fetch_drivers(race["session_key"])
    
    #results = fetch_session_results(race["session_key"])
    
    race_control = fetch_race_control(race["session_key"])
   
    
    print("Latest Race")
    print("-" * 40)
    print(f"Country : {race['country_name']}")
    print(f"Circuit : {race['circuit_short_name']}")
    print(f"Session : {race['session_name']}")
    print(f"Date    : {race['date_start']}")

    print("\nDrivers")
    print("-" * 40)

    for driver in drivers:
        print(
            f"{driver['driver_number']:>2} | "
            f"{driver['full_name']} | "
            f"{driver['team_name']}"
        )
    print(f"Race Control Events: {len(race_control)}")
    
    analyze_race_control(race_control)
    
if __name__ == "__main__":
    main()