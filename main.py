from api import fetch_latest_race

def main():
    race =fetch_latest_race()
    
    print("Latest Race")
    print("-"*40)
    print(f"Country : {race['country_name']}")
    print(f"Circuit : {race['circuit_short_name']}")
    print(f"Session : {race['session_name']}")
    print(f"Date : {race['date_start']}")
    
if __name__ == "__main__":
    main()