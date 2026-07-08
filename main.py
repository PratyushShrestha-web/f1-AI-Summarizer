from api import fetch_latest_race, fetch_drivers, fetch_session_results, fetch_race_control,fetch_driver_standings
from analyzer import analyze_race_control, build_prompt
from ai import generate_summary


def main():
    # Fetch the latest race
    race = fetch_latest_race()

    # Fetch all drivers for that race
    drivers = fetch_drivers(race["session_key"])
    
    #results = fetch_session_results(race["session_key"])
    
    race_control = fetch_race_control(race["session_key"])
    
    standings = fetch_driver_standings(race["session_key"])
    
  
    
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
    

    
    important_events = analyze_race_control(race_control)

    print("\nImportant Race Events")
    print("-" * 40)

    for event in important_events:
      print(
        f"Lap {event['lap']:>2} | "
        f"{event['flag']:<13} | "
        f"{event['message']}"
      )

    prompt = build_prompt(important_events)

    summary = generate_summary(prompt)

    print("\nAI Race Summary")
    print("-" * 40)
    print(summary)
    
    
    
if __name__ == "__main__":
    main()