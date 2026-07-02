from api import fetch_latest_race, fetch_drivers


def main():
    # Fetch the latest race
    race = fetch_latest_race()

    # Fetch all drivers for that race
    drivers = fetch_drivers(race["session_key"])

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


if __name__ == "__main__":
    main()